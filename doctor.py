from odoo import models, fields

class Doctor(models.model):
    _name='hospital.doctor'
    _description='doctor'

    name= fields.Char(string="name", required='True')
    speciality= fields.Char(string='speciality', required="True")
    patient_id= fields.Many2one('hospital.patient', string='Patient')

    def _compute_patient_count(self):
        for doctor in self:
            doctor.patient_count = len(doctor.patient_ids)





