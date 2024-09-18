
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
import os, re
from django.contrib import messages
from slickapp.models import visitorquery,servicesvisitorrequest
# from sendgrid.helpers.mail import Mail
# from sendgrid import SendGridAPIClient
from django.template.loader import render_to_string
from django.conf import settings

# Create your views here.

class home(TemplateView):
    template_name = 'home.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['home'] = 'active'
        return context

class about_us(TemplateView):
    template_name = 'about.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['about_us'] = 'active'
        return context


class services(TemplateView):
    template_name = 'services.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        services_visitor_obj = dict(servicesvisitorrequest._meta.get_field('services').choices)
        context['services'] = 'active'
        context['services_visitor_obj'] = services_visitor_obj
        return context

    def post(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        form_error = False
        Services = request.POST.get('services', None)
        full_name = request.POST.get('full_name', None)
        email = request.POST.get('email', None).lower()
        Message = request.POST.get('message', None)

          
        regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'
        if not(re.search(regex,email)):
          form_error = True
          messages.error(request, "Please enter valid email address!")

        if Services in ['', None]:
            messages.error(request, "Service is required..")
            form_error = True

        if full_name in ['', None]:
            messages.error(request, "Full Name is required..")
            form_error = True

        if Message in ['', None]:
            messages.error(request, "Message is required..")
            form_error = True


        if not(form_error):
          servicesvisitor = servicesvisitorrequest(services = Services,name = full_name, email = email, message = Message)
          servicesvisitor.save()
          
          html_message = render_to_string('email/contactusemail_services.html',{'services':Services, 'full_name':full_name,'email':email, 'Message':Message})
          if settings.SERVER_TYPE == 'production':
            to_email_list = ('marketing@panelviewpoint.com', 'Marketing Team')
          else:
            to_email_list = ('pythonteam@slickservices.in', 'Python Team')
          message = Mail(
              from_email = ('info@panelviewpoint.com','slick services Website Form'),
              to_emails= to_email_list,
              subject = 'slick services: New Website Contact Us Form Submission',
              html_content = html_message
              )
          try:
            sg = SendGridAPIClient('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')
            response = sg.send(message)
            messages.success(request, "Thank you for your message. We have received your message and our Sales person will get back to you as soon as possible.")
            context['alert_class'] = 'alert-success'
            context['email_message']='Thank you for your message. We will review and get back you.'
          except Exception as e:
            context['alert_class'] = 'alert-danger'
            context['email_message']='Something is wrong. Please try again!'
        return redirect('slickapp:services')



class contactus(TemplateView):
    template_name = 'contacts.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # visitor_obj = visitorquery.objects.all()
        visitor_query_obj = dict(visitorquery._meta.get_field('services').choices)
        context['contactus'] = 'active'
        context['visitor_query_obj'] = visitor_query_obj
        return context

    
    def post(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        data = request.POST
       
        form_error = False
        Services = data.get('services', None)
        Full_name = data.get('full_name', None)
        Email = data.get('email', None).lower()
        Message = data.get('message', None)
          
        regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'
        if not(re.search(regex,Email)):
            form_error = True
            messages.error(request, "Please enter valid email address!")

        if Services in ['', None]:
            messages.error(request, "Please Select Service Type")
            form_error = True

        if Full_name in ['', None]:
            messages.error(request, "Full Name is required..")
            form_error = True

        if Email in ['', None]:
            messages.error(request, "Email is required..")
            form_error = True

        if Message in ['', None]:
            messages.error(request, "Message is required..")
            form_error = True


        if not(form_error):
            visitor = visitorquery(services = Services ,name = Full_name,email = Email,  message = Message)
            visitor.save()
            
            html_message = render_to_string('email/contactusemail.html',{'Service':Services,'FullName':Full_name, 'Email':Email, 'Message':Message})
            # html_message = "<h1>Hello World</h1>"
            if settings.SERVER_TYPE == 'production':
                to_email_list = ('marketing@panelviewpoint.com', 'Marketing Team')
            else:
                # to_email_list = 'pythonteam@slickservices.in'
                to_email_list = ('pythonteam@slickservices.in', 'Python Team')
            message = Mail(
                from_email = ('info@panelviewpoint.com','Panel Viewpoint Website Form'),
                # from_email = 'info@panelviewpoint.com',
                to_emails= to_email_list,
                subject = 'Panel ViewPoint: New Website Contact Us Form Submission',
                html_content = html_message
                )
            try:
                sg = SendGridAPIClient('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')
                response = sg.send(message)
                messages.success(request, "Thank you for your message. We have received your message and our Sales person will get back to you as soon as possible.")
                context['alert_class'] = 'alert-success'
                context['email_message']='Thank you for your message. We will review and get back you.'
            except Exception as e:
                context['alert_class'] = 'alert-danger'
                context['email_message']='Something is wrong. Please try again!'
        return redirect('slickapp:contactus')



class ProjectManagementView(TemplateView):
    template_name = "project-management.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["project_management"] = "active"

        return context


class MobileDevelopmentView(TemplateView):
    template_name = "mobile-development.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["mobile_development"] = "active"

        return context


class CustomWebView(TemplateView):
    template_name = "custom-web.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["software_integration"] = "active"

        return context


class PanelWebDevelopmentView(TemplateView):
    template_name = "panel-web.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['panel_web'] = 'active'

        return context


class DigitalMarketingView(TemplateView):
    template_name = "digital-marketing.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['digital_marketing'] = 'active'

        return context


class CommunityRecruitmentView(TemplateView):
    template_name = "community-recruitment.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['community_recruitment'] = 'active'

        return context
    

class Terms_conditionsview(TemplateView):
    template_name = "terms_conditions.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['terms_conditions'] = 'active'

        return context
    
class Privacy_policyview(TemplateView):
    template_name = "privacy_policy.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['privacy_policy'] = 'active'

        return context