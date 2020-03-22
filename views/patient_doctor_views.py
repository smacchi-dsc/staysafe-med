from django.views import generic
from django.shortcuts import render
from django.http import Http404
from staysafemed.models.patient import Patient


class PatientsDoctorListView(generic.ListView):
    model = Patient
    context_object_name = 'patientsList'
    template_name = 'doctor/patients_list.html'

    def get_queryset(self):
        return sorted(Patient.objects.all(), key=lambda p: p.lastIllnessDataScore, reverse=True)


class PatientDoctorDetailView(generic.View):
    template = 'doctor/patient_detail.html'

    def get(self, request, *args, **kwargs):
        try: 
            patient = Patient.objects.get(pk=kwargs['id'])    
        except Patient.DoesNotExist:
            raise Http404("No matches the given query.")

        return render(request, self.template, {'patient': patient})


               
