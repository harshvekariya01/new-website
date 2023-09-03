from django.urls import path
from .views import *

app_name = 'slickapp'

urlpatterns = [

    # TemplateView
    path('', home.as_view(), name="home"),
    path('about', about_us.as_view(), name="abut_us"),
    path('services', services.as_view(), name="services"),
    path('contact-us', contactus.as_view(), name="contactus"),
    path('project-management', ProjectManagementView.as_view(), name="project_management_view"),
    path('mobile-development', MobileDevelopmentView.as_view(), name="mobile_development_view"),
    path('custom-web-development', CustomWebView.as_view(), name="custom_web_view"),
    path('panel-web-development', PanelWebDevelopmentView.as_view(), name="panel_web_view"),
    path('digital-marketing', DigitalMarketingView.as_view(), name="digital_marketing_view"),
    path('community-recruitment', CommunityRecruitmentView.as_view(), name="community_recruitment_view"),
    path('terms-conditions', Terms_conditionsview.as_view(), name="terms_conditions_view"),
    path('privacy-policy', Privacy_policyview.as_view(), name="privacy_policy_view"),
    

]
