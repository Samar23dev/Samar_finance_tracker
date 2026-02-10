from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .models import ChatMessage, BankStatement
from .openai_helper import ai_helper


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def chat(request):
    """Chat with AI bot"""
    message = request.data.get('message', '').strip()
    
    if not message:
        return Response({'error': 'Message required'}, status=400)
    
    # Get AI response
    response_text = ai_helper.chat(message)
    
    # Save to database
    ChatMessage.objects.create(
        user=request.user,
        message=message,
        response=response_text
    )
    
    return Response({
        'message': message,
        'response': response_text
    })


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def chat_history(request):
    """Get chat history"""
    messages = ChatMessage.objects.filter(user=request.user)[:20]
    data = [{
        'id': m.id,
        'message': m.message,
        'response': m.response,
        'created_at': m.created_at
    } for m in messages]
    return Response(data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def upload_statement(request):
    """Upload and analyze bank statement - Auto-create transactions"""
    if 'file' not in request.FILES:
        return Response({'error': 'No file uploaded'}, status=400)
    
    file_obj = request.FILES['file']
    file_name = file_obj.name
    
    # Validate file type
    if not (file_name.endswith('.pdf') or file_name.endswith('.csv')):
        return Response({'error': 'Only PDF and CSV files allowed'}, status=400)
    
    # Analyze with AI
    analysis = ai_helper.analyze_bank_statement(file_obj, file_name)
    
    # Auto-create transactions from statement
    file_obj.seek(0)  # Reset file pointer
    transactions_created = ai_helper.auto_create_transactions(request.user, file_obj, file_name)
    
    # Save to database
    statement = BankStatement.objects.create(
        user=request.user,
        file=file_obj,
        file_name=file_name,
        ai_analysis=analysis
    )
    
    return Response({
        'id': statement.id,
        'file_name': file_name,
        'analysis': analysis,
        'transactions_created': transactions_created,
        'uploaded_at': statement.uploaded_at
    })


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def statement_history(request):
    """Get uploaded statements"""
    statements = BankStatement.objects.filter(user=request.user)[:10]
    data = [{
        'id': s.id,
        'file_name': s.file_name,
        'analysis': s.ai_analysis,
        'uploaded_at': s.uploaded_at
    } for s in statements]
    return Response(data)
