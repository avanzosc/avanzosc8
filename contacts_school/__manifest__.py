# Copyright 2019 Alfredo de la Fuente - AvanzOSC
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html
{
    "name": "Contacts School",
    "version": "12.0.1.0.0",
    "license": "AGPL-3",
    "depends": [
        "contacts",
        "hr"
    ],
    "author": "AvanzOSC",
    "website": "http://www.avanzosc.es",
    "category": "Tools",
    "data": [
        "data/ir_sequence_data.xml",
        "security/ir.model.access.csv",
        "views/res_partner_view.xml",
        "views/res_partner_association_federation_view.xml",
        "views/res_partner_family_view.xml",
        "views/res_partner_information_type_view.xml",
        "views/res_partner_information_view.xml",
        "views/res_partner_student_characteristic_view.xml",
        "views/res_partner_student_payer_view.xml",
    ],
    "installable": True,
}