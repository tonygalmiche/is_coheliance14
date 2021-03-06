# -*- coding: utf-8 -*-

from odoo import api, fields, models

class ResPartner(models.Model):
    _inherit = 'res.partner'


    def open_partner_form_view(self):
        dummy, view_id = self.env['ir.model.data'].get_object_reference('base', 'view_partner_form')
        for partner in self:
            return {
                'name':"Contact",
                'view_mode': 'form',
                'view_id': view_id,
                'view_type': 'form',
                'res_model': 'res.partner',
                'type': 'ir.actions.act_window',
                'res_id': partner.id,
                'domain': '[]',
            }


    def _affaire_count(self):
        for obj in self:
            affaires=self.env['is.affaire'].search([('client_id', '=', obj.id)])
            obj.affaire_count=len(affaires)


    is_prenom                   = fields.Char("Prénom")
    is_code_fournisseur         = fields.Char("Code comptable fournisseur")
    is_siret                    = fields.Char("N°SIRET")
    is_num_declaration_activite = fields.Char("N° déclaration activité", help="N° de déclaration d'activité obligatoire pour les sous-traitants")
    is_ape                      = fields.Char("APE")
    is_secteur_activite_id      = fields.Many2one('is.secteur.activite', "Secteur d'activité", required=False)
    is_typologie_id             = fields.Many2one('is.typologie', "Typologie")
    is_region_id                = fields.Many2one('is.region', 'Région', required=False)
    is_classification_id        = fields.Many2one('is.classification', 'Classification', required=False)
    is_bp                       = fields.Char("Boite postale")
    is_liste_diffusion          = fields.Char("Liste de diffusion")
    is_email_perso              = fields.Char("Courriel personnel")
    is_responsable              = fields.Boolean("Responsable structure", help="Est le responsable légal de la structure")
    affaire_count               = fields.Integer(compute=_affaire_count, string='# Affaires')


    # def name_get(self, cr, uid, ids, context=None):
    #     if context is None:
    #         context = {}
    #     if isinstance(ids, (int, long)):
    #         ids = [ids]
    #     res = []
    #     for record in self.browse(cr, uid, ids, context=context):
    #         name=record.name
    #         if record.is_prenom:
    #             name = record.is_prenom  + ' ' +record.name
    #         if record.parent_id and not record.is_company:
    #             name = "%s, %s" % (record.parent_name, name)
    #         if context.get('show_address_only'):
    #             name = self._display_address(cr, uid, record, without_company=True, context=context)
    #         if context.get('show_address'):
    #             name = name + "\n" + self._display_address(cr, uid, record, without_company=True, context=context)
    #         name = name.replace('\n\n','\n')
    #         name = name.replace('\n\n','\n')
    #         if context.get('show_email') and record.email:
    #             name = "%s <%s>" % (name, record.email)
    #         res.append((record.id, name))
    #     return res




class res_company(models.Model):
    _inherit = 'res.company'

    taux_km = fields.Float("Taux indemnité kilométrique ", required=False)


class is_region(models.Model):
    _name = 'is.region'
    _description = "Région"

    name = fields.Char("Région", required=True)


class is_secteur_activite(models.Model):
    _name = 'is.secteur.activite'
    _description = "Secteur d'activité"

    name = fields.Char("Secteur d'activité", required=True)


class is_typologie(models.Model):
    _name = 'is.typologie'
    _description = "Typologie"

    name = fields.Char("Typologie", required=True)


class is_classification(models.Model):
    _name = 'is.classification'
    _description = "Classification"
    
    name = fields.Char("Classification", required=True)


class is_base_documentaire(models.Model):
    _name = 'is.base.documentaire'
    _description = "Base documentaire"
    
    name = fields.Char("Nom du document", required=True)

