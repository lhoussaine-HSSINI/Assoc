from django.urls import path
from .views import (AssociationAdminSignup,CustomAuthToken,
                    AssociationMemberSignup ,OrganizationAdminSignup,add_association,add_membre,add_organization)
from . import views
from rest_framework import routers
from django.conf.urls import include

router=routers.DefaultRouter()
router.register('Association', add_association)
router.register('Member', add_membre)
router.register('Organization', add_organization)

urlpatterns = [
    path('signup/Aadmin', AssociationAdminSignup.as_view()),
    path('signup/Amember', AssociationMemberSignup.as_view()),
    path('signup/Oadmin', OrganizationAdminSignup.as_view()),
    path('rest/Glist/', views.GtList.as_view()),
    path('rest/Gdetail/<int:pk>', views.GDetail.as_view()),
    path('api/loginAMA/',CustomAuthToken.as_view(), name='auth-token'),
    path('Association_List/', views.AssociationList.as_view()),
    path('Add_AMO_API/', include(router.urls)),

]
