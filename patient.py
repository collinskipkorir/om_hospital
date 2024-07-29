from odoo import models, fields, api
from odoo.exceptions import ValidationError

class Patient(models.Model):
    _name = 'hospital.patient'
    _description = 'Patient'

    name = fields.Char(string="Name", required=True)
    age = fields.Interger(string="Age", required=True)
    date_of_birth = fields.Date(string='Date of Birth', required= True)
    gender = fields.Selection(
        [
            ('male', 'Male'),
            ('female', 'Female'),
            ('others', 'Others'),
        ],
        string="Gender"
    )

    doctor_id = fields.Many2one('hospital.doctor', string='Doctor')

    @api.depends('doctor_id')
    def _compute_patient_count(self):
        for patient in self:
            patient.doctor_count = len(patient.doctor_id)

    @api.constrains('doctor_id')
    def check_unique_doctor(self):
        for patient in self:
            if self.search_count([('doctor_id', '=', patient.doctor_id.id)]) > 1:
                raise ValidationError('Each doctor can only serve one patient!')
