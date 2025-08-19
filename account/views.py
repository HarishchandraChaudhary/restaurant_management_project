from django.shortcuts import render,get_object_or_404
from django.httpimport JsonResponse
from django.db import DatabaseError,IntegrityError, transaction
from django.core.exceptions import ValidationError,ObjectDoesNotExit
from django.contrib.auth.models import User
import logging
import json

# Create your views here.
logger = logging.get_Logger(__name__)
def user_profile_view(request,user_id):
    """
    Simple view to handle user profiles with comprensive error handling 
    """
    try:
        # Validate uer_id parameter
        try:
            user_id = int(user_id)
        except(ValueError,TypeError):
            logger.warning(f"Invalid user ID format:{user_id}")
            return JsonResponse({
                'error':'Invalid user ID',
                'message':'User ID must be valid number',

            },status=400)
        # Handle GET request - Reterive user profile
        if request.method == 'GET':
            try:
                user = User.objects.get(id=user_id)
                #Prepare response data
                user_data = {
                    'id':user.id,
                    'username':user.username,
                    'email':user.email,
                    'first_name':user.first_name,
                    'last_name':user.last_name,
                    'is_active':user.is_active,
                    'data_joined':user.data_joined.isoformat()
                }
                logger.info(f"Successfully retrieved user profile for ID:{user_id}")
                return JsonResponse({
                    'success':True,
                    'data':user_data
                },stat=200)
            except User.DoesNotExist:
                logger.warning(f"User not found with ID:{user_id}")
                return JsonResponse({
                    'error':"User not found",
                    'message':f'No user exists with ID {user_id}'
                },status=404)
            except DatabaseError as e:
                logger.error(f"Database error while fetching user:{str(e)}")
                return JsonResponse({
                    'error':'Database error',
                    'message':'Unable to retrieve user data due to database issues'
                },status=500)
        elif request.method == 'POST':
            try:
                try:
                    data = json.loads(request.body)
                except json.JSONDecodeError:
                    logger.warning("invalid JSON data received")
                    return JsonResponse({

                        'error':'Invalid JSON',
                        'message':'Request body must contain valid JSON data'
                    },status=400)

                    # User database transaction for data intergrity
                     with transation.atomic():
                        try:
                            # Get user from database
                            user = User.objects.get(i=user_id)
                            if 'first_name' in data:
                                user.first_name = data['first_name']
                            if 'last_name'in data:
                                user.last_name = data['last_name']
                            if 'email'in data:
                                 user.email = data['email']

                                user.full_clean()
                                user.save()
                                logger.info(f"Successfully updated user profile for ID:{user_id}")
                                return JsonResponse({
                                    'success':True,
                                    'message':'User profile updated successfully',
                                    'data':{
                                        'id':user.id,
                                        'username':user.username,
                                        'email':user.email,
                                        'first_name':user.first_name,
                                        'last_name':user.last_name
                                    }
                                },status=200)
                        except ValidationError as e:
                             logger.warning(f"Validation error during user update:{str(e)"})

                             return JsonResponse({
                                'error':'Validation error',
                                'message':'Invalid data provided',
                                'details':e.message_dict if hasattr(e,'message_dict') else str(e)

                             },status=400) 
                                                    