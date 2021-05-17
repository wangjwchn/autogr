import sys
sys.path.append("../../")

from z3 import *
from Rigi.axioms import *
from Rigi.checker import *
from Rigi.table import *
from Rigi.tableIns import *
from Rigi.argvbuilder import *

##############################################################################################

BloodGroupingRh = Table('BloodGroupingRh')
BloodGroupingRh.addAttr('tst_bloodG_id', Table.Type.STRING)
BloodGroupingRh.addAttr('prescription_id', Table.Type.STRING)
BloodGroupingRh.addAttr('bloodGroup', Table.Type.STRING)
BloodGroupingRh.addAttr('rhesusD', Table.Type.STRING)
BloodGroupingRh.addAttr('appointment_id', Table.Type.STRING)
BloodGroupingRh.addAttr('date', Table.Type.INT)
BloodGroupingRh.setPKey('tst_bloodG_id')
BloodGroupingRh.build()


LipidTest = Table('LipidTest')
LipidTest.addAttr('tst_li_id', Table.Type.STRING)
LipidTest.addAttr('prescription_id', Table.Type.STRING)
LipidTest.addAttr('cholestrolHDL', Table.Type.STRING)
LipidTest.addAttr('cholestrolLDL', Table.Type.STRING)
LipidTest.addAttr('triglycerides', Table.Type.STRING)
LipidTest.addAttr('totalCholestrolLDLHDLratio', Table.Type.STRING)
LipidTest.addAttr('appointment_id', Table.Type.STRING)
LipidTest.addAttr('date', Table.Type.INT)
LipidTest.setPKey('tst_li_id')
LipidTest.build()


LiverFunctionTest = Table('LiverFunctionTest')
LiverFunctionTest.addAttr('tst_liver_id', Table.Type.STRING)
LiverFunctionTest.addAttr('prescription_id', Table.Type.STRING)
LiverFunctionTest.addAttr('totalProtein', Table.Type.REAL)
LiverFunctionTest.addAttr('albumin', Table.Type.REAL)
LiverFunctionTest.addAttr('globulin', Table.Type.REAL)
LiverFunctionTest.addAttr('totalBilirubin', Table.Type.REAL)
LiverFunctionTest.addAttr('directBilirubin', Table.Type.REAL)
LiverFunctionTest.addAttr('sgotast', Table.Type.REAL)
LiverFunctionTest.addAttr('sgptalt', Table.Type.REAL)
LiverFunctionTest.addAttr('alkalinePhospates', Table.Type.REAL)
LiverFunctionTest.addAttr('appointment_id', Table.Type.STRING)
LiverFunctionTest.addAttr('date', Table.Type.INT)
LiverFunctionTest.setPKey('tst_liver_id')
LiverFunctionTest.build()


RenalFunctionTest = Table('RenalFunctionTest')
RenalFunctionTest.addAttr('tst_renal_id', Table.Type.STRING)
RenalFunctionTest.addAttr('prescription_id', Table.Type.STRING)
RenalFunctionTest.addAttr('creatinine', Table.Type.REAL)
RenalFunctionTest.addAttr('urea', Table.Type.REAL)
RenalFunctionTest.addAttr('totalBilirubin', Table.Type.REAL)
RenalFunctionTest.addAttr('directBilirubin', Table.Type.REAL)
RenalFunctionTest.addAttr('sgotast', Table.Type.REAL)
RenalFunctionTest.addAttr('sgptalt', Table.Type.REAL)
RenalFunctionTest.addAttr('alkalinePhospates', Table.Type.REAL)
RenalFunctionTest.addAttr('appointment_id', Table.Type.STRING)
RenalFunctionTest.addAttr('date', Table.Type.INT)
RenalFunctionTest.setPKey('tst_renal_id')
RenalFunctionTest.build()


SeriumCreatinePhosphokinase = Table('SeriumCreatinePhosphokinase')
SeriumCreatinePhosphokinase.addAttr('tst_SCP_id', Table.Type.STRING)
SeriumCreatinePhosphokinase.addAttr('prescription_id', Table.Type.STRING)
SeriumCreatinePhosphokinase.addAttr('hiv12ELISA', Table.Type.STRING)
SeriumCreatinePhosphokinase.addAttr('appointment_id', Table.Type.STRING)
SeriumCreatinePhosphokinase.addAttr('date', Table.Type.INT)
SeriumCreatinePhosphokinase.setPKey('tst_SCP_id')
SeriumCreatinePhosphokinase.build()


SeriumCreatinePhosphokinaseTotal = Table('SeriumCreatinePhosphokinaseTotal')
SeriumCreatinePhosphokinaseTotal.addAttr('tst_SCPT_id', Table.Type.STRING)
SeriumCreatinePhosphokinaseTotal.addAttr('test_id', Table.Type.STRING)
SeriumCreatinePhosphokinaseTotal.addAttr('prescription_id', Table.Type.STRING)
SeriumCreatinePhosphokinaseTotal.addAttr('cpkTotal', Table.Type.INT)
SeriumCreatinePhosphokinaseTotal.addAttr('appointment_id', Table.Type.STRING)
SeriumCreatinePhosphokinaseTotal.addAttr('date', Table.Type.INT)
SeriumCreatinePhosphokinaseTotal.setPKey('tst_SCPT_id')
SeriumCreatinePhosphokinaseTotal.build()


UrineFullReport = Table('UrineFullReport')
UrineFullReport.addAttr('tst_ur_id', Table.Type.STRING)
UrineFullReport.addAttr('prescription_id', Table.Type.STRING)
UrineFullReport.addAttr('appearance', Table.Type.STRING)
UrineFullReport.addAttr('sgRefractometer', Table.Type.STRING)
UrineFullReport.addAttr('ph', Table.Type.REAL)
UrineFullReport.addAttr('protein', Table.Type.STRING)
UrineFullReport.addAttr('glucose', Table.Type.STRING)
UrineFullReport.addAttr('ketoneBodies', Table.Type.STRING)
UrineFullReport.addAttr('bilirubin', Table.Type.STRING)
UrineFullReport.addAttr('urobilirubin', Table.Type.STRING)
UrineFullReport.addAttr('contrifugedDepositsphaseContrastMicroscopy', Table.Type.STRING)
UrineFullReport.addAttr('pusCells', Table.Type.STRING)
UrineFullReport.addAttr('redCells', Table.Type.STRING)
UrineFullReport.addAttr('epithelialCells', Table.Type.STRING)
UrineFullReport.addAttr('casts', Table.Type.STRING)
UrineFullReport.addAttr('cristals', Table.Type.STRING)
UrineFullReport.addAttr('appointment_id', Table.Type.STRING)
UrineFullReport.addAttr('date', Table.Type.INT)
UrineFullReport.setPKey('tst_ur_id')
UrineFullReport.build()


appointment = Table('appointment')
appointment.addAttr('appointment_id', Table.Type.STRING)
appointment.addAttr('date', Table.Type.INT)
appointment.addAttr('info', Table.Type.STRING)
appointment.addAttr('patient_id', Table.Type.STRING)
appointment.addAttr('bill_id', Table.Type.STRING)
appointment.addAttr('slmc_reg_no', Table.Type.STRING)
appointment.addAttr('cancelled', Table.Type.INT)
appointment.setPKey('appointment_id')
appointment.build()


bill = Table('bill')
bill.addAttr('bill_id', Table.Type.STRING)
bill.addAttr('bill_date', Table.Type.INT)
bill.addAttr('doctor_fee', Table.Type.INT)
bill.addAttr('hospital_fee', Table.Type.INT)
bill.addAttr('pharmacy_fee', Table.Type.INT)
bill.addAttr('laboratory_fee', Table.Type.INT)
bill.addAttr('appointment_fee', Table.Type.INT)
bill.addAttr('vat', Table.Type.INT)
bill.addAttr('discount', Table.Type.INT)
bill.addAttr('total', Table.Type.INT)
bill.addAttr('payment_method', Table.Type.STRING)
bill.addAttr('consultant_id', Table.Type.STRING)
bill.addAttr('patient_id', Table.Type.STRING)
bill.addAttr('refund', Table.Type.INT)
bill.setPKey('bill_id')
bill.build()


completeBloodCount = Table('completeBloodCount')
completeBloodCount.addAttr('tst_CBC_id', Table.Type.STRING)
completeBloodCount.addAttr('prescription_id', Table.Type.STRING)
completeBloodCount.addAttr('totalWhiteCellCount', Table.Type.INT)
completeBloodCount.addAttr('differentialCount', Table.Type.INT)
completeBloodCount.addAttr('neutrophils', Table.Type.INT)
completeBloodCount.addAttr('lymphocytes', Table.Type.INT)
completeBloodCount.addAttr('monocytes', Table.Type.INT)
completeBloodCount.addAttr('eosonophils', Table.Type.INT)
completeBloodCount.addAttr('basophils', Table.Type.INT)
completeBloodCount.addAttr('haemoglobin', Table.Type.REAL)
completeBloodCount.addAttr('redBloodCells', Table.Type.REAL)
completeBloodCount.addAttr('meanCellVolume', Table.Type.REAL)
completeBloodCount.addAttr('haematocrit', Table.Type.REAL)
completeBloodCount.addAttr('meanCellHaemoglobin', Table.Type.REAL)
completeBloodCount.addAttr('mchConcentration', Table.Type.REAL)
completeBloodCount.addAttr('redCellsDistributionWidth', Table.Type.REAL)
completeBloodCount.addAttr('plateletCount', Table.Type.INT)
completeBloodCount.addAttr('appointment_id', Table.Type.STRING)
completeBloodCount.addAttr('date', Table.Type.INT)
completeBloodCount.setPKey('tst_CBC_id')
completeBloodCount.build()


diagnose_history = Table('diagnose_history')
diagnose_history.addAttr('diagnostic_id', Table.Type.STRING)
diagnose_history.addAttr('patient_id', Table.Type.STRING)
diagnose_history.addAttr('diagnose', Table.Type.STRING)
diagnose_history.addAttr('date', Table.Type.INT)
diagnose_history.addAttr('consultant_id', Table.Type.STRING)
diagnose_history.addAttr('prescription_id', Table.Type.STRING)
diagnose_history.setPKey('diagnostic_id')
diagnose_history.build()


doctor = Table('doctor')
doctor.addAttr('slmc_reg_no', Table.Type.STRING)
doctor.addAttr('user_id', Table.Type.STRING)
doctor.addAttr('education', Table.Type.STRING)
doctor.addAttr('training', Table.Type.STRING)
doctor.addAttr('experienced_areas', Table.Type.STRING)
doctor.addAttr('experience', Table.Type.STRING)
doctor.addAttr('achievements', Table.Type.STRING)
doctor.addAttr('channelling_fee', Table.Type.INT)
doctor.setPKey('slmc_reg_no')
doctor.build()


doctor_availability = Table('doctor_availability')
doctor_availability.addAttr('time_slot_id', Table.Type.STRING)
doctor_availability.addAttr('slmc_reg_no', Table.Type.STRING)
doctor_availability.addAttr('day', Table.Type.INT)
doctor_availability.addAttr('time_slot', Table.Type.STRING)
doctor_availability.addAttr('current_week_appointments', Table.Type.INT)
doctor_availability.addAttr('next_week_appointments', Table.Type.INT)
doctor_availability.setPKey('time_slot_id')
doctor_availability.setPKey('time_slot','slmc_reg_no','day')
doctor_availability.build()


drug = Table('drug')
drug.addAttr('drug_id', Table.Type.STRING)
drug.addAttr('drug_name', Table.Type.STRING)
drug.addAttr('dangerous_drug', Table.Type.INT)
drug.setPKey('drug_id')
drug.build()


drug_brand_names = Table('drug_brand_names')
drug_brand_names.addAttr('brand_id', Table.Type.STRING)
drug_brand_names.addAttr('brand_name', Table.Type.STRING)
drug_brand_names.addAttr('generic_name', Table.Type.STRING)
drug_brand_names.addAttr('drug_type', Table.Type.STRING)
drug_brand_names.addAttr('drug_unit', Table.Type.STRING)
drug_brand_names.addAttr('unit_price', Table.Type.INT)
drug_brand_names.setPKey('brand_id')
drug_brand_names.build()


lab_appointment = Table('lab_appointment')
lab_appointment.addAttr('lab_appointment_id', Table.Type.STRING)
lab_appointment.addAttr('test_id', Table.Type.STRING)
lab_appointment.addAttr('date', Table.Type.INT)
lab_appointment.addAttr('info', Table.Type.STRING)
lab_appointment.addAttr('patient_id', Table.Type.STRING)
lab_appointment.addAttr('bill_id', Table.Type.STRING)
lab_appointment.addAttr('lab_assistant_id', Table.Type.STRING)
lab_appointment.addAttr('cancelled', Table.Type.INT)
lab_appointment.addAttr('doctor_id', Table.Type.STRING)
lab_appointment.setPKey('lab_appointment_id')
lab_appointment.build()


lab_appointment_timetable = Table('lab_appointment_timetable')
lab_appointment_timetable.addAttr('app_id', Table.Type.STRING)
lab_appointment_timetable.addAttr('app_test_id', Table.Type.STRING)
lab_appointment_timetable.addAttr('app_day', Table.Type.INT)
lab_appointment_timetable.addAttr('time_slot', Table.Type.STRING)
lab_appointment_timetable.addAttr('current_week_appointments', Table.Type.INT)
lab_appointment_timetable.addAttr('next_week_appointments', Table.Type.INT)
lab_appointment_timetable.setPKey('app_id')
lab_appointment_timetable.build()


lab_assistant = Table('lab_assistant')
lab_assistant.addAttr('lab_assistant_id', Table.Type.STRING)
lab_assistant.addAttr('user_id', Table.Type.STRING)
lab_assistant.addAttr('education', Table.Type.STRING)
lab_assistant.addAttr('training', Table.Type.STRING)
lab_assistant.addAttr('experience', Table.Type.STRING)
lab_assistant.addAttr('achievements', Table.Type.STRING)
lab_assistant.setPKey('lab_assistant_id')
lab_assistant.build()


lab_test = Table('lab_test')
lab_test.addAttr('test_id', Table.Type.STRING)
lab_test.addAttr('test_name', Table.Type.STRING)
lab_test.addAttr('test_description', Table.Type.STRING)
lab_test.addAttr('test_fee', Table.Type.INT)
lab_test.setPKey('test_id')
lab_test.build()


medical_history = Table('medical_history')
medical_history.addAttr('history_id', Table.Type.STRING)
medical_history.addAttr('patient_id', Table.Type.STRING)
medical_history.addAttr('doctor_id', Table.Type.STRING)
medical_history.addAttr('date', Table.Type.INT)
medical_history.addAttr('history', Table.Type.STRING)
medical_history.setPKey('history_id')
medical_history.build()


patient = Table('patient')
patient.addAttr('patient_id', Table.Type.STRING)
patient.addAttr('person_id', Table.Type.STRING)
patient.addAttr('drug_allergies_and_reactions', Table.Type.STRING)
patient.setPKey('patient_id')
patient.build()


patient_message_receive = Table('patient_message_receive')
patient_message_receive.addAttr('message_id', Table.Type.STRING)
patient_message_receive.addAttr('receiver', Table.Type.STRING)
patient_message_receive.addAttr('sender', Table.Type.STRING)
patient_message_receive.addAttr('subject', Table.Type.STRING)
patient_message_receive.addAttr('message', Table.Type.STRING)
patient_message_receive.addAttr('date', Table.Type.INT)
patient_message_receive.setPKey('message_id')
patient_message_receive.build()


patient_message_send = Table('patient_message_send')
patient_message_send.addAttr('message_id', Table.Type.STRING)
patient_message_send.addAttr('receiver', Table.Type.STRING)
patient_message_send.addAttr('sender', Table.Type.STRING)
patient_message_send.addAttr('email', Table.Type.STRING)
patient_message_send.addAttr('message', Table.Type.STRING)
patient_message_send.addAttr('date', Table.Type.INT)
patient_message_send.setPKey('message_id')
patient_message_send.build()


patient_useraccount = Table('patient_useraccount')
patient_useraccount.addAttr('patient_id', Table.Type.STRING)
patient_useraccount.addAttr('person_id', Table.Type.STRING)
patient_useraccount.addAttr('username', Table.Type.STRING)
patient_useraccount.addAttr('password', Table.Type.STRING)
patient_useraccount.setPKey('patient_id')
patient_useraccount.build()


person = Table('person')
person.addAttr('person_id', Table.Type.STRING)
person.addAttr('user_id', Table.Type.STRING)
person.addAttr('nic', Table.Type.STRING)
person.addAttr('gender', Table.Type.STRING)
person.addAttr('date_of_birth', Table.Type.INT)
person.addAttr('address', Table.Type.STRING)
person.addAttr('mobile', Table.Type.STRING)
person.addAttr('first_name', Table.Type.STRING)
person.addAttr('last_name', Table.Type.STRING)
person.addAttr('email', Table.Type.STRING)
person.addAttr('nationality', Table.Type.STRING)
person.addAttr('religion', Table.Type.STRING)
person.setPKey('person_id')
person.build()


pharmacist = Table('pharmacist')
pharmacist.addAttr('pharmacist_id', Table.Type.STRING)
pharmacist.addAttr('user_id', Table.Type.STRING)
pharmacist.addAttr('education', Table.Type.STRING)
pharmacist.addAttr('training', Table.Type.STRING)
pharmacist.addAttr('experience', Table.Type.STRING)
pharmacist.addAttr('achievements', Table.Type.STRING)
pharmacist.setPKey('pharmacist_id')
pharmacist.build()


pharmacy_history = Table('pharmacy_history')
pharmacy_history.addAttr('history_id', Table.Type.STRING)
pharmacy_history.addAttr('prescription_id', Table.Type.STRING)
pharmacy_history.addAttr('bill_id', Table.Type.STRING)
pharmacy_history.addAttr('date', Table.Type.INT)
pharmacy_history.addAttr('no_of_drugs', Table.Type.INT)
pharmacy_history.addAttr('excluded', Table.Type.STRING)
pharmacy_history.setPKey('history_id')
pharmacy_history.build()


pharmacy_stock = Table('pharmacy_stock')
pharmacy_stock.addAttr('stock_id', Table.Type.STRING)
pharmacy_stock.addAttr('drug_id', Table.Type.STRING)
pharmacy_stock.addAttr('brand_id', Table.Type.STRING)
pharmacy_stock.addAttr('stock', Table.Type.INT)
pharmacy_stock.addAttr('remaining_quantity', Table.Type.INT)
pharmacy_stock.addAttr('manufac_date', Table.Type.INT)
pharmacy_stock.addAttr('exp_date', Table.Type.INT)
pharmacy_stock.addAttr('supplier_id', Table.Type.STRING)
pharmacy_stock.addAttr('date', Table.Type.INT)
pharmacy_stock.setPKey('stock_id')
pharmacy_stock.build()


prescription = Table('prescription')
prescription.addAttr('prescription_id', Table.Type.STRING)
prescription.addAttr('patient_id', Table.Type.STRING)
prescription.addAttr('consultant_id', Table.Type.STRING)
prescription.addAttr('date', Table.Type.INT)
prescription.addAttr('drugs_dose', Table.Type.STRING)
prescription.addAttr('tests', Table.Type.STRING)
prescription.setPKey('prescription_id')
prescription.build()


refund = Table('refund')
refund.addAttr('refund_id', Table.Type.STRING)
refund.addAttr('bill_id', Table.Type.STRING)
refund.addAttr('payment_type', Table.Type.STRING)
refund.addAttr('reason', Table.Type.STRING)
refund.addAttr('amount', Table.Type.INT)
refund.addAttr('date', Table.Type.INT)
refund.setPKey('refund_id')
refund.build()


signup = Table('signup')
signup.addAttr('id', Table.Type.INT)
signup.addAttr('fname', Table.Type.STRING)
signup.addAttr('lname', Table.Type.STRING)
signup.addAttr('nic', Table.Type.STRING)
signup.addAttr('address', Table.Type.STRING)
signup.addAttr('contact', Table.Type.INT)
signup.addAttr('email', Table.Type.STRING)
signup.addAttr('gender', Table.Type.STRING)
signup.addAttr('dob', Table.Type.STRING)
signup.addAttr('religion', Table.Type.STRING)
signup.addAttr('nationality', Table.Type.STRING)
signup.addAttr('maritalstatus', Table.Type.STRING)
signup.addAttr('medicalhistory', Table.Type.STRING)
signup.addAttr('username', Table.Type.STRING)
signup.addAttr('password', Table.Type.STRING)
signup.setPKey('id')
signup.build()


suppliers = Table('suppliers')
suppliers.addAttr('supplier_id', Table.Type.STRING)
suppliers.addAttr('supplier_name', Table.Type.STRING)
suppliers.setPKey('supplier_id')
suppliers.build()


sys_user = Table('sys_user')
sys_user.addAttr('person_id', Table.Type.STRING)
sys_user.addAttr('user_id', Table.Type.STRING)
sys_user.addAttr('user_name', Table.Type.STRING)
sys_user.addAttr('user_type', Table.Type.STRING)
sys_user.addAttr('other_info', Table.Type.STRING)
sys_user.addAttr('password', Table.Type.STRING)
sys_user.addAttr('online', Table.Type.INT)
sys_user.addAttr('login', Table.Type.INT)
sys_user.addAttr('logout', Table.Type.INT)
sys_user.addAttr('profile_pic', Table.Type.STRING)
sys_user.addAttr('suspend', Table.Type.INT)
sys_user.setPKey('user_id')
sys_user.build()


tempappointment = Table('tempappointment')
tempappointment.addAttr('id', Table.Type.INT)
tempappointment.addAttr('doctor_id', Table.Type.STRING)
tempappointment.addAttr('time', Table.Type.INT)
tempappointment.addAttr('date', Table.Type.INT)
tempappointment.addAttr('patient_id', Table.Type.STRING)
tempappointment.setPKey('id')
tempappointment.build()


tmp_bill = Table('tmp_bill')
tmp_bill.addAttr('tmp_bill_id', Table.Type.STRING)
tmp_bill.addAttr('doctor_fee', Table.Type.INT)
tmp_bill.addAttr('hospital_fee', Table.Type.INT)
tmp_bill.addAttr('pharmacy_fee', Table.Type.INT)
tmp_bill.addAttr('laboratory_fee', Table.Type.INT)
tmp_bill.addAttr('appointment_fee', Table.Type.INT)
tmp_bill.addAttr('vat', Table.Type.INT)
tmp_bill.addAttr('discount', Table.Type.INT)
tmp_bill.addAttr('consultant_id', Table.Type.STRING)
tmp_bill.addAttr('patient_id', Table.Type.STRING)
tmp_bill.setPKey('tmp_bill_id')
tmp_bill.setPKey('patient_id')
tmp_bill.build()


user_message = Table('user_message')
user_message.addAttr('message_id', Table.Type.STRING)
user_message.addAttr('reciver', Table.Type.STRING)
user_message.addAttr('sender', Table.Type.STRING)
user_message.addAttr('subject', Table.Type.STRING)
user_message.addAttr('message', Table.Type.STRING)
user_message.addAttr('date', Table.Type.INT)
user_message.addAttr('rd', Table.Type.INT)
user_message.setPKey('message_id')
user_message.build()


website_messages = Table('website_messages')
website_messages.addAttr('id', Table.Type.INT)
website_messages.addAttr('first_name', Table.Type.STRING)
website_messages.addAttr('last_name', Table.Type.STRING)
website_messages.addAttr('email', Table.Type.STRING)
website_messages.addAttr('message', Table.Type.STRING)
website_messages.setPKey('id')
website_messages.build()


def GenState():
    TABLE_BloodGroupingRh = TableInstance(BloodGroupingRh)
    TABLE_LipidTest = TableInstance(LipidTest)
    TABLE_LiverFunctionTest = TableInstance(LiverFunctionTest)
    TABLE_RenalFunctionTest = TableInstance(RenalFunctionTest)
    TABLE_SeriumCreatinePhosphokinase = TableInstance(SeriumCreatinePhosphokinase)
    TABLE_SeriumCreatinePhosphokinaseTotal = TableInstance(SeriumCreatinePhosphokinaseTotal)
    TABLE_UrineFullReport = TableInstance(UrineFullReport)
    TABLE_appointment = TableInstance(appointment)
    TABLE_bill = TableInstance(bill)
    TABLE_completeBloodCount = TableInstance(completeBloodCount)
    TABLE_diagnose_history = TableInstance(diagnose_history)
    TABLE_doctor = TableInstance(doctor)
    TABLE_doctor_availability = TableInstance(doctor_availability)
    TABLE_drug = TableInstance(drug)
    TABLE_drug_brand_names = TableInstance(drug_brand_names)
    TABLE_lab_appointment = TableInstance(lab_appointment)
    TABLE_lab_appointment_timetable = TableInstance(lab_appointment_timetable)
    TABLE_lab_assistant = TableInstance(lab_assistant)
    TABLE_lab_test = TableInstance(lab_test)
    TABLE_medical_history = TableInstance(medical_history)
    TABLE_patient = TableInstance(patient)
    TABLE_patient_message_receive = TableInstance(patient_message_receive)
    TABLE_patient_message_send = TableInstance(patient_message_send)
    TABLE_patient_useraccount = TableInstance(patient_useraccount)
    TABLE_person = TableInstance(person)
    TABLE_pharmacist = TableInstance(pharmacist)
    TABLE_pharmacy_history = TableInstance(pharmacy_history)
    TABLE_pharmacy_stock = TableInstance(pharmacy_stock)
    TABLE_prescription = TableInstance(prescription)
    TABLE_refund = TableInstance(refund)
    TABLE_signup = TableInstance(signup)
    TABLE_suppliers = TableInstance(suppliers)
    TABLE_sys_user = TableInstance(sys_user)
    TABLE_tempappointment = TableInstance(tempappointment)
    TABLE_tmp_bill = TableInstance(tmp_bill)
    TABLE_user_message = TableInstance(user_message)
    TABLE_website_messages = TableInstance(website_messages)
    return {'TABLE_BloodGroupingRh': TABLE_BloodGroupingRh,'TABLE_LipidTest': TABLE_LipidTest,'TABLE_LiverFunctionTest': TABLE_LiverFunctionTest,'TABLE_RenalFunctionTest': TABLE_RenalFunctionTest,'TABLE_SeriumCreatinePhosphokinase': TABLE_SeriumCreatinePhosphokinase,'TABLE_SeriumCreatinePhosphokinaseTotal': TABLE_SeriumCreatinePhosphokinaseTotal,'TABLE_UrineFullReport': TABLE_UrineFullReport,'TABLE_appointment': TABLE_appointment,'TABLE_bill': TABLE_bill,'TABLE_completeBloodCount': TABLE_completeBloodCount,'TABLE_diagnose_history': TABLE_diagnose_history,'TABLE_doctor': TABLE_doctor,'TABLE_doctor_availability': TABLE_doctor_availability,'TABLE_drug': TABLE_drug,'TABLE_drug_brand_names': TABLE_drug_brand_names,'TABLE_lab_appointment': TABLE_lab_appointment,'TABLE_lab_appointment_timetable': TABLE_lab_appointment_timetable,'TABLE_lab_assistant': TABLE_lab_assistant,'TABLE_lab_test': TABLE_lab_test,'TABLE_medical_history': TABLE_medical_history,'TABLE_patient': TABLE_patient,'TABLE_patient_message_receive': TABLE_patient_message_receive,'TABLE_patient_message_send': TABLE_patient_message_send,'TABLE_patient_useraccount': TABLE_patient_useraccount,'TABLE_person': TABLE_person,'TABLE_pharmacist': TABLE_pharmacist,'TABLE_pharmacy_history': TABLE_pharmacy_history,'TABLE_pharmacy_stock': TABLE_pharmacy_stock,'TABLE_prescription': TABLE_prescription,'TABLE_refund': TABLE_refund,'TABLE_signup': TABLE_signup,'TABLE_suppliers': TABLE_suppliers,'TABLE_sys_user': TABLE_sys_user,'TABLE_tempappointment': TABLE_tempappointment,'TABLE_tmp_bill': TABLE_tmp_bill,'TABLE_user_message': TABLE_user_message,'TABLE_website_messages': TABLE_website_messages}

def GenArgv():
    builder = ArgvBuilder()
    builder.NewOp('Op_Doctor_doctorTimeTableAddSlot_run_8412')
    builder.AddArgv('newTimeSlotId', ArgvBuilder.Type.STRING)
    builder.AddArgv('slmcReg', ArgvBuilder.Type.STRING)
    builder.AddArgv('day', ArgvBuilder.Type.INT)
    builder.AddArgv('timeSlot', ArgvBuilder.Type.STRING)
    builder.AddArgv('currentWeekAppointments', ArgvBuilder.Type.INT)
    builder.AddArgv('nextWeekAppointments', ArgvBuilder.Type.INT)

    builder.NewOp('Op_Pharmacist_addNewDrug2_run_8413')
    builder.AddArgv('newDrugId', ArgvBuilder.Type.STRING)
    builder.AddArgv('drugName', ArgvBuilder.Type.STRING)

    builder.NewOp('Op_Cashier_bill_run_8414')
    builder.AddArgv('newBillId', ArgvBuilder.Type.STRING)
    builder.AddArgv('date', ArgvBuilder.Type.INT)
    builder.AddArgv('doctorFee', ArgvBuilder.Type.INT)
    builder.AddArgv('hospitalFee', ArgvBuilder.Type.INT)
    builder.AddArgv('pharmacyFee', ArgvBuilder.Type.INT)
    builder.AddArgv('laboratoryFee', ArgvBuilder.Type.INT)
    builder.AddArgv('appointmentFee', ArgvBuilder.Type.INT)
    builder.AddArgv('vat', ArgvBuilder.Type.INT)
    builder.AddArgv('discount', ArgvBuilder.Type.INT)
    builder.AddArgv('total', ArgvBuilder.Type.INT)
    builder.AddArgv('paymentMethod', ArgvBuilder.Type.STRING)
    builder.AddArgv('consultantId', ArgvBuilder.Type.STRING)
    builder.AddArgv('patientId', ArgvBuilder.Type.STRING)
    builder.AddArgv('refund', ArgvBuilder.Type.INT)

    builder.NewOp('Op_Pharmacist_updateStock_run_8415')
    builder.AddArgv('newStockId', ArgvBuilder.Type.STRING)
    builder.AddArgv('drugId', ArgvBuilder.Type.STRING)
    builder.AddArgv('brandId', ArgvBuilder.Type.STRING)
    builder.AddArgv('stock', ArgvBuilder.Type.INT)
    builder.AddArgv('manuDate', ArgvBuilder.Type.INT)
    builder.AddArgv('expDate', ArgvBuilder.Type.INT)
    builder.AddArgv('suppId', ArgvBuilder.Type.STRING)
    builder.AddArgv('date', ArgvBuilder.Type.INT)

    builder.NewOp('Op_Pharmacist_reduceStock_run_8416')
    builder.AddArgv('id', ArgvBuilder.Type.STRING)
    builder.AddArgv('pharmacy_stock_stock_id', ArgvBuilder.Type.STRING)

    builder.NewOp('Op_LabAssistant_updateLabAssistantInfo_run_8417')
    builder.AddArgv('id', ArgvBuilder.Type.STRING)
    builder.AddArgv('lab_assistant_lab_assistant_id', ArgvBuilder.Type.STRING)

    builder.NewOp('Op_Receptionist_updateAccountInfo_run_8418')
    builder.AddArgv('id', ArgvBuilder.Type.STRING)
    builder.AddArgv('doctor_user_id', ArgvBuilder.Type.STRING)
    builder.AddArgv('sys_user_user_id', ArgvBuilder.Type.STRING)

    builder.NewOp('Op_Doctor_diagnose_run_8419')
    builder.AddArgv('newHistoryId', ArgvBuilder.Type.STRING)
    builder.AddArgv('patientId', ArgvBuilder.Type.STRING)
    builder.AddArgv('doctorId', ArgvBuilder.Type.STRING)
    builder.AddArgv('date', ArgvBuilder.Type.INT)
    builder.AddArgv('history', ArgvBuilder.Type.STRING)

    builder.NewOp('Op_Pharmacist_updateAccountInfo_run_8420')
    builder.AddArgv('pharmacistId', ArgvBuilder.Type.STRING)
    builder.AddArgv('pharmacist_user_id', ArgvBuilder.Type.STRING)
    builder.AddArgv('sys_user_user_id', ArgvBuilder.Type.STRING)

    builder.NewOp('Op_LabAssistant_UrineFullReport_run_8421')
    builder.AddArgv('newTstId', ArgvBuilder.Type.STRING)
    builder.AddArgv('appId', ArgvBuilder.Type.STRING)
    builder.AddArgv('appearance', ArgvBuilder.Type.STRING)
    builder.AddArgv('sgRefractometer', ArgvBuilder.Type.STRING)
    builder.AddArgv('ph', ArgvBuilder.Type.REAL)
    builder.AddArgv('protein', ArgvBuilder.Type.STRING)
    builder.AddArgv('glucose', ArgvBuilder.Type.STRING)
    builder.AddArgv('ketoneBodies', ArgvBuilder.Type.STRING)
    builder.AddArgv('bilirubin', ArgvBuilder.Type.STRING)
    builder.AddArgv('urobilirubin', ArgvBuilder.Type.STRING)
    builder.AddArgv('contrifugedDepositsphaseContrastMicroscopy', ArgvBuilder.Type.STRING)
    builder.AddArgv('pusCells', ArgvBuilder.Type.STRING)
    builder.AddArgv('redCells', ArgvBuilder.Type.STRING)
    builder.AddArgv('epithelialCells', ArgvBuilder.Type.STRING)
    builder.AddArgv('casts', ArgvBuilder.Type.STRING)
    builder.AddArgv('cristals', ArgvBuilder.Type.STRING)
    builder.AddArgv('now', ArgvBuilder.Type.INT)

    builder.NewOp('Op_Receptionist_cancelAppointment_run_8422')
    builder.AddArgv('appointmentId', ArgvBuilder.Type.STRING)
    builder.AddArgv('appointment_appointment_id', ArgvBuilder.Type.STRING)
    builder.AddArgv('appointment_bill_id', ArgvBuilder.Type.STRING)
    builder.AddArgv('newRefundId', ArgvBuilder.Type.STRING)
    builder.AddArgv('bill_total', ArgvBuilder.Type.INT)
    builder.AddArgv('now', ArgvBuilder.Type.INT)
    builder.AddArgv('bill_bill_id', ArgvBuilder.Type.STRING)

    builder.NewOp('Op_Cashier_makeRefund_run_8423')
    builder.AddArgv('id', ArgvBuilder.Type.STRING)

    builder.NewOp('Op_Cashier_refund_run_8424')
    builder.AddArgv('newRefundId', ArgvBuilder.Type.STRING)
    builder.AddArgv('billId', ArgvBuilder.Type.STRING)
    builder.AddArgv('paymentType', ArgvBuilder.Type.STRING)
    builder.AddArgv('reason', ArgvBuilder.Type.STRING)
    builder.AddArgv('amount', ArgvBuilder.Type.INT)
    builder.AddArgv('now', ArgvBuilder.Type.INT)

    builder.NewOp('Op_Doctor_allergies_run_8425')
    builder.AddArgv('patientId', ArgvBuilder.Type.STRING)
    builder.AddArgv('patient_drug_allergies_and_reactions', ArgvBuilder.Type.STRING)
    builder.AddArgv('allergies', ArgvBuilder.Type.STRING)
    builder.AddArgv('patient_patient_id', ArgvBuilder.Type.STRING)

    builder.NewOp('Op_Admin_createNewUser_run_8426')
    builder.AddArgv('newPersonId', ArgvBuilder.Type.STRING)
    builder.AddArgv('firstName', ArgvBuilder.Type.STRING)
    builder.AddArgv('lastName', ArgvBuilder.Type.STRING)
    builder.AddArgv('nic', ArgvBuilder.Type.STRING)
    builder.AddArgv('mobile', ArgvBuilder.Type.STRING)
    builder.AddArgv('newUserId', ArgvBuilder.Type.STRING)
    builder.AddArgv('userName', ArgvBuilder.Type.STRING)
    builder.AddArgv('userType', ArgvBuilder.Type.STRING)
    builder.AddArgv('newLabAssistantId', ArgvBuilder.Type.STRING)
    builder.AddArgv('newPharmacistId', ArgvBuilder.Type.STRING)
    builder.AddArgv('newSlmcReg', ArgvBuilder.Type.STRING)

    builder.NewOp('Op_Pharmacist_bill_run_8427')
    builder.AddArgv('id', ArgvBuilder.Type.STRING)
    builder.AddArgv('tmp_bill_tmp_bill_id', ArgvBuilder.Type.STRING)

    builder.NewOp('Op_Receptionist_updatePatientInfo_run_8428')
    builder.AddArgv('patientId', ArgvBuilder.Type.STRING)
    builder.AddArgv('info', ArgvBuilder.Type.STRING)
    builder.AddArgv('patient_patient_id', ArgvBuilder.Type.STRING)

    builder.NewOp('Op_Doctor_updateDoctorInfo_run_8429')
    builder.AddArgv('id', ArgvBuilder.Type.STRING)
    builder.AddArgv('doctor_slmc_reg_no', ArgvBuilder.Type.STRING)

    builder.NewOp('Op_Receptionist_updateProfileInfo_run_8430')
    builder.AddArgv('userId', ArgvBuilder.Type.STRING)
    builder.AddArgv('address', ArgvBuilder.Type.STRING)
    builder.AddArgv('sys_user_person_id', ArgvBuilder.Type.STRING)
    builder.AddArgv('person_person_id', ArgvBuilder.Type.STRING)

    builder.NewOp('Op_LabAssistant_SeriumCreatinePhosphokinaseTotal_run_8431')
    builder.AddArgv('newTstId', ArgvBuilder.Type.STRING)
    builder.AddArgv('appId', ArgvBuilder.Type.STRING)
    builder.AddArgv('cpkTotal', ArgvBuilder.Type.INT)
    builder.AddArgv('now', ArgvBuilder.Type.INT)

    builder.NewOp('Op_Cashier_updateAccountInfo_run_8432')
    builder.AddArgv('id', ArgvBuilder.Type.STRING)
    builder.AddArgv('sys_user_user_id', ArgvBuilder.Type.STRING)

    builder.NewOp('Op_Admin_suspendUser_run_8433')
    builder.AddArgv('id', ArgvBuilder.Type.STRING)
    builder.AddArgv('sys_user_user_id', ArgvBuilder.Type.STRING)

    builder.NewOp('Op_Doctor_updateProfileInfo_run_8434')
    builder.AddArgv('id', ArgvBuilder.Type.STRING)
    builder.AddArgv('doctor_user_id', ArgvBuilder.Type.STRING)
    builder.AddArgv('sys_user_person_id', ArgvBuilder.Type.STRING)
    builder.AddArgv('person_person_id', ArgvBuilder.Type.STRING)

    builder.NewOp('Op_Pharmacist_updateProfileInfo_run_8435')
    builder.AddArgv('id', ArgvBuilder.Type.STRING)
    builder.AddArgv('address', ArgvBuilder.Type.STRING)
    builder.AddArgv('sys_user_person_id', ArgvBuilder.Type.STRING)
    builder.AddArgv('person_person_id', ArgvBuilder.Type.STRING)

    builder.NewOp('Op_Doctor_bill_run_8436')
    builder.AddArgv('id', ArgvBuilder.Type.STRING)
    builder.AddArgv('tmp_bill_tmp_bill_id', ArgvBuilder.Type.STRING)

    builder.NewOp('Op_LabAssistant_BloodGroupingTest_run_8437')
    builder.AddArgv('newTstId', ArgvBuilder.Type.STRING)
    builder.AddArgv('appId', ArgvBuilder.Type.STRING)
    builder.AddArgv('bloodGroup', ArgvBuilder.Type.STRING)
    builder.AddArgv('rh', ArgvBuilder.Type.STRING)
    builder.AddArgv('now', ArgvBuilder.Type.INT)

    builder.NewOp('Op_Doctor_prescribe_run_8438')
    builder.AddArgv('newPrescId', ArgvBuilder.Type.STRING)
    builder.AddArgv('patientId', ArgvBuilder.Type.STRING)
    builder.AddArgv('consultantId', ArgvBuilder.Type.STRING)
    builder.AddArgv('date', ArgvBuilder.Type.INT)
    builder.AddArgv('drugDose', ArgvBuilder.Type.STRING)
    builder.AddArgv('tests', ArgvBuilder.Type.STRING)

    builder.NewOp('Op_Receptionist_setPatientInfo_run_8439')
    builder.AddArgv('newPersonId', ArgvBuilder.Type.STRING)
    builder.AddArgv('newPatientId', ArgvBuilder.Type.STRING)
    builder.AddArgv('nic', ArgvBuilder.Type.STRING)
    builder.AddArgv('gender', ArgvBuilder.Type.STRING)
    builder.AddArgv('birth', ArgvBuilder.Type.INT)
    builder.AddArgv('address', ArgvBuilder.Type.STRING)
    builder.AddArgv('mobile', ArgvBuilder.Type.STRING)
    builder.AddArgv('firstName', ArgvBuilder.Type.STRING)
    builder.AddArgv('lastName', ArgvBuilder.Type.STRING)
    builder.AddArgv('email', ArgvBuilder.Type.STRING)
    builder.AddArgv('nationality', ArgvBuilder.Type.STRING)
    builder.AddArgv('religion', ArgvBuilder.Type.STRING)
    builder.AddArgv('patientInfo', ArgvBuilder.Type.STRING)

    builder.NewOp('Op_LabAssistant_RenalFunctionTest_run_8440')
    builder.AddArgv('newTstId', ArgvBuilder.Type.STRING)
    builder.AddArgv('appId', ArgvBuilder.Type.STRING)
    builder.AddArgv('creatinine', ArgvBuilder.Type.REAL)
    builder.AddArgv('urea', ArgvBuilder.Type.REAL)
    builder.AddArgv('totalBilirubin', ArgvBuilder.Type.REAL)
    builder.AddArgv('directBilirubin', ArgvBuilder.Type.REAL)
    builder.AddArgv('sgotast', ArgvBuilder.Type.REAL)
    builder.AddArgv('sgptalt', ArgvBuilder.Type.REAL)
    builder.AddArgv('alkalinePhospates', ArgvBuilder.Type.REAL)
    builder.AddArgv('now', ArgvBuilder.Type.INT)

    builder.NewOp('Op_Admin_updateProfileInfo_run_8441')
    builder.AddArgv('id', ArgvBuilder.Type.STRING)
    builder.AddArgv('sys_user_person_id', ArgvBuilder.Type.STRING)
    builder.AddArgv('person_person_id', ArgvBuilder.Type.STRING)

    builder.NewOp('Op_Admin_resetPassword_run_8442')
    builder.AddArgv('id', ArgvBuilder.Type.STRING)
    builder.AddArgv('sys_user_user_id', ArgvBuilder.Type.STRING)

    builder.NewOp('Op_Receptionist_refund_run_8443')
    builder.AddArgv('newRefundId', ArgvBuilder.Type.STRING)
    builder.AddArgv('billId', ArgvBuilder.Type.STRING)
    builder.AddArgv('paymentType', ArgvBuilder.Type.STRING)
    builder.AddArgv('reason', ArgvBuilder.Type.STRING)
    builder.AddArgv('amount', ArgvBuilder.Type.INT)
    builder.AddArgv('now', ArgvBuilder.Type.INT)

    builder.NewOp('Op_Admin_unsuspendUser_run_8444')
    builder.AddArgv('id', ArgvBuilder.Type.STRING)
    builder.AddArgv('sys_user_user_id', ArgvBuilder.Type.STRING)

    builder.NewOp('Op_Receptionist_makeLabAppointment_run_8445')
    builder.AddArgv('newAppId', ArgvBuilder.Type.STRING)
    builder.AddArgv('testId', ArgvBuilder.Type.STRING)
    builder.AddArgv('patientId', ArgvBuilder.Type.STRING)
    builder.AddArgv('doctorId', ArgvBuilder.Type.STRING)
    builder.AddArgv('currentDate', ArgvBuilder.Type.INT)
    builder.AddArgv('day', ArgvBuilder.Type.INT)
    builder.AddArgv('lab_test_test_fee', ArgvBuilder.Type.INT)
    builder.AddArgv('tmp_bill_tmp_bill_id', ArgvBuilder.Type.STRING)
    builder.AddArgv('newTmpBillId', ArgvBuilder.Type.STRING)

    builder.NewOp('Op_LabAssistant_LipidTest_run_8446')
    builder.AddArgv('newTstId', ArgvBuilder.Type.STRING)
    builder.AddArgv('appId', ArgvBuilder.Type.STRING)
    builder.AddArgv('cholestrolHDL', ArgvBuilder.Type.STRING)
    builder.AddArgv('cholestrolLDL', ArgvBuilder.Type.STRING)
    builder.AddArgv('triglycerides', ArgvBuilder.Type.STRING)
    builder.AddArgv('totalCholestrolLDLHDLratio', ArgvBuilder.Type.STRING)
    builder.AddArgv('now', ArgvBuilder.Type.INT)

    builder.NewOp('Op_Doctor_updateAccountInfo_run_8447')
    builder.AddArgv('id', ArgvBuilder.Type.STRING)
    builder.AddArgv('doctor_user_id', ArgvBuilder.Type.STRING)
    builder.AddArgv('sys_user_user_id', ArgvBuilder.Type.STRING)

    builder.NewOp('Op_LabAssistant_completeBloodCount_run_8448')
    builder.AddArgv('newTstId', ArgvBuilder.Type.STRING)
    builder.AddArgv('appId', ArgvBuilder.Type.STRING)
    builder.AddArgv('totalWhiteCellCount', ArgvBuilder.Type.INT)
    builder.AddArgv('differentialCount', ArgvBuilder.Type.INT)
    builder.AddArgv('neutrophils', ArgvBuilder.Type.INT)
    builder.AddArgv('lymphocytes', ArgvBuilder.Type.INT)
    builder.AddArgv('monocytes', ArgvBuilder.Type.INT)
    builder.AddArgv('eosonophils', ArgvBuilder.Type.INT)
    builder.AddArgv('basophils', ArgvBuilder.Type.INT)
    builder.AddArgv('haemoglobin', ArgvBuilder.Type.REAL)
    builder.AddArgv('redBloodCells', ArgvBuilder.Type.REAL)
    builder.AddArgv('meanCellVolume', ArgvBuilder.Type.REAL)
    builder.AddArgv('haematocrit', ArgvBuilder.Type.REAL)
    builder.AddArgv('meanCellHaemoglobin', ArgvBuilder.Type.REAL)
    builder.AddArgv('mchConcentration', ArgvBuilder.Type.REAL)
    builder.AddArgv('redCellsDistributionWidth', ArgvBuilder.Type.REAL)
    builder.AddArgv('plateletCount', ArgvBuilder.Type.INT)
    builder.AddArgv('now', ArgvBuilder.Type.INT)

    builder.NewOp('Op_Receptionist_makeAppointment_run_8449')
    builder.AddArgv('newAppId', ArgvBuilder.Type.STRING)
    builder.AddArgv('patientId', ArgvBuilder.Type.STRING)
    builder.AddArgv('doctorId', ArgvBuilder.Type.STRING)
    builder.AddArgv('currentDate', ArgvBuilder.Type.INT)
    builder.AddArgv('day', ArgvBuilder.Type.INT)
    builder.AddArgv('timeSlot', ArgvBuilder.Type.STRING)
    builder.AddArgv('doctor_availability_time_slot', ArgvBuilder.Type.STRING)
    builder.AddArgv('doctor_availability_slmc_reg_no', ArgvBuilder.Type.STRING)
    builder.AddArgv('doctor_availability_day', ArgvBuilder.Type.INT)
    builder.AddArgv('tmp_bill_tmp_bill_id', ArgvBuilder.Type.STRING)
    builder.AddArgv('newTmpBillId', ArgvBuilder.Type.STRING)

    builder.NewOp('Op_Pharmacist_addNewSupplier_run_8450')
    builder.AddArgv('newSupplierId', ArgvBuilder.Type.STRING)
    builder.AddArgv('name', ArgvBuilder.Type.STRING)

    builder.NewOp('Op_Pharmacist_updatePharmacistInfo_run_8451')
    builder.AddArgv('id', ArgvBuilder.Type.STRING)
    builder.AddArgv('pharmacist_pharmacist_id', ArgvBuilder.Type.STRING)

    builder.NewOp('Op_LabAssistant_updateProfileInfo_run_8452')
    builder.AddArgv('id', ArgvBuilder.Type.STRING)
    builder.AddArgv('sys_user_person_id', ArgvBuilder.Type.STRING)
    builder.AddArgv('person_person_id', ArgvBuilder.Type.STRING)

    builder.NewOp('Op_Cashier_removeFromTempBill_run_8453')
    builder.AddArgv('id', ArgvBuilder.Type.STRING)

    builder.NewOp('Op_LabAssistant_liverFunctionTest_run_8454')
    builder.AddArgv('newTstId', ArgvBuilder.Type.STRING)
    builder.AddArgv('appId', ArgvBuilder.Type.STRING)
    builder.AddArgv('totalBilirubin', ArgvBuilder.Type.REAL)
    builder.AddArgv('albumin', ArgvBuilder.Type.REAL)
    builder.AddArgv('globulin', ArgvBuilder.Type.REAL)
    builder.AddArgv('directBilirubin', ArgvBuilder.Type.REAL)
    builder.AddArgv('sgotast', ArgvBuilder.Type.REAL)
    builder.AddArgv('sgptalt', ArgvBuilder.Type.REAL)
    builder.AddArgv('alkalinePhospates', ArgvBuilder.Type.REAL)
    builder.AddArgv('now', ArgvBuilder.Type.INT)

    builder.NewOp('Op_Receptionist_cancelLabAppointment_run_8455')
    builder.AddArgv('labAppointmentId', ArgvBuilder.Type.STRING)
    builder.AddArgv('lab_appointment_lab_appointment_id', ArgvBuilder.Type.STRING)
    builder.AddArgv('lab_appointment_bill_id', ArgvBuilder.Type.STRING)
    builder.AddArgv('newRefundId', ArgvBuilder.Type.STRING)
    builder.AddArgv('bill_total', ArgvBuilder.Type.INT)
    builder.AddArgv('now', ArgvBuilder.Type.INT)
    builder.AddArgv('bill_bill_id', ArgvBuilder.Type.STRING)

    builder.NewOp('Op_Pharmacist_addNewBrand_run_8456')
    builder.AddArgv('newBrandId', ArgvBuilder.Type.STRING)
    builder.AddArgv('brandName', ArgvBuilder.Type.STRING)
    builder.AddArgv('genericName', ArgvBuilder.Type.STRING)
    builder.AddArgv('drugType', ArgvBuilder.Type.STRING)
    builder.AddArgv('drugUnit', ArgvBuilder.Type.STRING)
    builder.AddArgv('unitPrice', ArgvBuilder.Type.INT)

    builder.NewOp('Op_LabAssistant_SeriumCreatinePhosphokinase_run_8457')
    builder.AddArgv('newTstId', ArgvBuilder.Type.STRING)
    builder.AddArgv('appId', ArgvBuilder.Type.STRING)
    builder.AddArgv('hiv12ELISA', ArgvBuilder.Type.STRING)
    builder.AddArgv('now', ArgvBuilder.Type.INT)

    builder.NewOp('Op_Doctor_removeDoctorTime_run_8458')
    builder.AddArgv('id', ArgvBuilder.Type.STRING)

    builder.NewOp('Op_Admin_updateAccountInfo_run_8459')
    builder.AddArgv('id', ArgvBuilder.Type.STRING)
    builder.AddArgv('sys_user_user_id', ArgvBuilder.Type.STRING)

    builder.NewOp('Op_LabAssistant_updateAccountInfo_run_8460')
    builder.AddArgv('id', ArgvBuilder.Type.STRING)
    builder.AddArgv('doctor_user_id', ArgvBuilder.Type.STRING)
    builder.AddArgv('sys_user_user_id', ArgvBuilder.Type.STRING)

    builder.NewOp('Op_Cashier_updateProfileInfo_run_8461')
    builder.AddArgv('id', ArgvBuilder.Type.STRING)
    builder.AddArgv('sys_user_person_id', ArgvBuilder.Type.STRING)

    return builder.Build()

class Op_Doctor_doctorTimeTableAddSlot_run_8412():
    def __init__(self):
        self.sops = [(self.cond0, self.csop0, self.sop0)]
        self.axiom = AxiomEmpty()

    def cond0(self, state, argv):
        newTimeSlotId = argv['Op_Doctor_doctorTimeTableAddSlot_run_8412']['newTimeSlotId']
        slmcReg = argv['Op_Doctor_doctorTimeTableAddSlot_run_8412']['slmcReg']
        day = argv['Op_Doctor_doctorTimeTableAddSlot_run_8412']['day']
        timeSlot = argv['Op_Doctor_doctorTimeTableAddSlot_run_8412']['timeSlot']
        currentWeekAppointments = argv['Op_Doctor_doctorTimeTableAddSlot_run_8412']['currentWeekAppointments']
        nextWeekAppointments = argv['Op_Doctor_doctorTimeTableAddSlot_run_8412']['nextWeekAppointments']
        return (state['TABLE_doctor_availability'].notNil({'time_slot_id': argv['Op_Doctor_doctorTimeTableAddSlot_run_8412']['newTimeSlotId']}) == False)

    def csop0(self, state, argv):
        return True

    def sop0(self, state, argv):
        newTimeSlotId = argv['Op_Doctor_doctorTimeTableAddSlot_run_8412']['newTimeSlotId']
        slmcReg = argv['Op_Doctor_doctorTimeTableAddSlot_run_8412']['slmcReg']
        day = argv['Op_Doctor_doctorTimeTableAddSlot_run_8412']['day']
        timeSlot = argv['Op_Doctor_doctorTimeTableAddSlot_run_8412']['timeSlot']
        currentWeekAppointments = argv['Op_Doctor_doctorTimeTableAddSlot_run_8412']['currentWeekAppointments']
        nextWeekAppointments = argv['Op_Doctor_doctorTimeTableAddSlot_run_8412']['nextWeekAppointments']
        doctor_availability_time_slot_id = argv['Op_Doctor_doctorTimeTableAddSlot_run_8412']['newTimeSlotId']
        doctor_availability_slmc_reg_no = argv['Op_Doctor_doctorTimeTableAddSlot_run_8412']['slmcReg']
        doctor_availability_day = argv['Op_Doctor_doctorTimeTableAddSlot_run_8412']['day']
        doctor_availability_time_slot = argv['Op_Doctor_doctorTimeTableAddSlot_run_8412']['timeSlot']
        doctor_availability_current_week_appointments = argv['Op_Doctor_doctorTimeTableAddSlot_run_8412']['currentWeekAppointments']
        doctor_availability_next_week_appointments = argv['Op_Doctor_doctorTimeTableAddSlot_run_8412']['nextWeekAppointments']
        state['TABLE_doctor_availability'].add({'time_slot_id': doctor_availability_time_slot_id}, {'slmc_reg_no': doctor_availability_slmc_reg_no,'day': doctor_availability_day,'time_slot': doctor_availability_time_slot,'current_week_appointments': doctor_availability_current_week_appointments,'next_week_appointments': doctor_availability_next_week_appointments})
        return state


class Op_Pharmacist_addNewDrug2_run_8413():
    def __init__(self):
        self.sops = [(self.cond0, self.csop0, self.sop0)]
        self.axiom = AxiomEmpty()

    def cond0(self, state, argv):
        newDrugId = argv['Op_Pharmacist_addNewDrug2_run_8413']['newDrugId']
        drugName = argv['Op_Pharmacist_addNewDrug2_run_8413']['drugName']
        return (state['TABLE_drug'].notNil({'drug_id': argv['Op_Pharmacist_addNewDrug2_run_8413']['newDrugId']}) == False)

    def csop0(self, state, argv):
        return True

    def sop0(self, state, argv):
        newDrugId = argv['Op_Pharmacist_addNewDrug2_run_8413']['newDrugId']
        drugName = argv['Op_Pharmacist_addNewDrug2_run_8413']['drugName']
        drug_drug_id = argv['Op_Pharmacist_addNewDrug2_run_8413']['newDrugId']
        drug_drug_name = argv['Op_Pharmacist_addNewDrug2_run_8413']['drugName']
        drug_dangerous_drug = 0
        state['TABLE_drug'].add({'drug_id': drug_drug_id}, {'drug_name': drug_drug_name,'dangerous_drug': drug_dangerous_drug})
        return state


class Op_Cashier_bill_run_8414():
    def __init__(self):
        self.sops = [(self.cond0, self.csop0, self.sop0)]
        self.axiom = AxiomEmpty()

    def cond0(self, state, argv):
        newBillId = argv['Op_Cashier_bill_run_8414']['newBillId']
        date = argv['Op_Cashier_bill_run_8414']['date']
        doctorFee = argv['Op_Cashier_bill_run_8414']['doctorFee']
        hospitalFee = argv['Op_Cashier_bill_run_8414']['hospitalFee']
        pharmacyFee = argv['Op_Cashier_bill_run_8414']['pharmacyFee']
        laboratoryFee = argv['Op_Cashier_bill_run_8414']['laboratoryFee']
        appointmentFee = argv['Op_Cashier_bill_run_8414']['appointmentFee']
        vat = argv['Op_Cashier_bill_run_8414']['vat']
        discount = argv['Op_Cashier_bill_run_8414']['discount']
        total = argv['Op_Cashier_bill_run_8414']['total']
        paymentMethod = argv['Op_Cashier_bill_run_8414']['paymentMethod']
        consultantId = argv['Op_Cashier_bill_run_8414']['consultantId']
        patientId = argv['Op_Cashier_bill_run_8414']['patientId']
        refund = argv['Op_Cashier_bill_run_8414']['refund']
        return True

    def csop0(self, state, argv):
        return True

    def sop0(self, state, argv):
        newBillId = argv['Op_Cashier_bill_run_8414']['newBillId']
        date = argv['Op_Cashier_bill_run_8414']['date']
        doctorFee = argv['Op_Cashier_bill_run_8414']['doctorFee']
        hospitalFee = argv['Op_Cashier_bill_run_8414']['hospitalFee']
        pharmacyFee = argv['Op_Cashier_bill_run_8414']['pharmacyFee']
        laboratoryFee = argv['Op_Cashier_bill_run_8414']['laboratoryFee']
        appointmentFee = argv['Op_Cashier_bill_run_8414']['appointmentFee']
        vat = argv['Op_Cashier_bill_run_8414']['vat']
        discount = argv['Op_Cashier_bill_run_8414']['discount']
        total = argv['Op_Cashier_bill_run_8414']['total']
        paymentMethod = argv['Op_Cashier_bill_run_8414']['paymentMethod']
        consultantId = argv['Op_Cashier_bill_run_8414']['consultantId']
        patientId = argv['Op_Cashier_bill_run_8414']['patientId']
        refund = argv['Op_Cashier_bill_run_8414']['refund']
        bill_bill_id = argv['Op_Cashier_bill_run_8414']['newBillId']
        bill_bill_date = argv['Op_Cashier_bill_run_8414']['date']
        bill_doctor_fee = argv['Op_Cashier_bill_run_8414']['doctorFee']
        bill_hospital_fee = argv['Op_Cashier_bill_run_8414']['hospitalFee']
        bill_pharmacy_fee = argv['Op_Cashier_bill_run_8414']['pharmacyFee']
        bill_laboratory_fee = argv['Op_Cashier_bill_run_8414']['laboratoryFee']
        bill_appointment_fee = argv['Op_Cashier_bill_run_8414']['appointmentFee']
        bill_vat = argv['Op_Cashier_bill_run_8414']['vat']
        bill_discount = argv['Op_Cashier_bill_run_8414']['discount']
        bill_total = argv['Op_Cashier_bill_run_8414']['total']
        bill_payment_method = argv['Op_Cashier_bill_run_8414']['paymentMethod']
        bill_consultant_id = argv['Op_Cashier_bill_run_8414']['consultantId']
        bill_patient_id = argv['Op_Cashier_bill_run_8414']['patientId']
        bill_refund = argv['Op_Cashier_bill_run_8414']['refund']
        state['TABLE_bill'].add({'bill_id': bill_bill_id}, {'bill_date': bill_bill_date,'doctor_fee': bill_doctor_fee,'hospital_fee': bill_hospital_fee,'pharmacy_fee': bill_pharmacy_fee,'laboratory_fee': bill_laboratory_fee,'appointment_fee': bill_appointment_fee,'vat': bill_vat,'discount': bill_discount,'total': bill_total,'payment_method': bill_payment_method,'consultant_id': bill_consultant_id,'patient_id': bill_patient_id,'refund': bill_refund})
        return state


class Op_Pharmacist_updateStock_run_8415():
    def __init__(self):
        self.sops = [(self.cond0, self.csop0, self.sop0)]
        self.axiom = AxiomEmpty()

    def cond0(self, state, argv):
        newStockId = argv['Op_Pharmacist_updateStock_run_8415']['newStockId']
        drugId = argv['Op_Pharmacist_updateStock_run_8415']['drugId']
        brandId = argv['Op_Pharmacist_updateStock_run_8415']['brandId']
        stock = argv['Op_Pharmacist_updateStock_run_8415']['stock']
        manuDate = argv['Op_Pharmacist_updateStock_run_8415']['manuDate']
        expDate = argv['Op_Pharmacist_updateStock_run_8415']['expDate']
        suppId = argv['Op_Pharmacist_updateStock_run_8415']['suppId']
        date = argv['Op_Pharmacist_updateStock_run_8415']['date']
        return (state['TABLE_pharmacy_stock'].notNil({'stock_id': argv['Op_Pharmacist_updateStock_run_8415']['newStockId']}) == False)

    def csop0(self, state, argv):
        return True

    def sop0(self, state, argv):
        newStockId = argv['Op_Pharmacist_updateStock_run_8415']['newStockId']
        drugId = argv['Op_Pharmacist_updateStock_run_8415']['drugId']
        brandId = argv['Op_Pharmacist_updateStock_run_8415']['brandId']
        stock = argv['Op_Pharmacist_updateStock_run_8415']['stock']
        manuDate = argv['Op_Pharmacist_updateStock_run_8415']['manuDate']
        expDate = argv['Op_Pharmacist_updateStock_run_8415']['expDate']
        suppId = argv['Op_Pharmacist_updateStock_run_8415']['suppId']
        date = argv['Op_Pharmacist_updateStock_run_8415']['date']
        pharmacy_stock_stock_id = argv['Op_Pharmacist_updateStock_run_8415']['newStockId']
        pharmacy_stock_drug_id = argv['Op_Pharmacist_updateStock_run_8415']['drugId']
        pharmacy_stock_brand_id = argv['Op_Pharmacist_updateStock_run_8415']['brandId']
        pharmacy_stock_stock = argv['Op_Pharmacist_updateStock_run_8415']['stock']
        pharmacy_stock_remaining_quantity = argv['Op_Pharmacist_updateStock_run_8415']['stock']
        pharmacy_stock_manufac_date = argv['Op_Pharmacist_updateStock_run_8415']['manuDate']
        pharmacy_stock_exp_date = argv['Op_Pharmacist_updateStock_run_8415']['expDate']
        pharmacy_stock_supplier_id = argv['Op_Pharmacist_updateStock_run_8415']['suppId']
        pharmacy_stock_date = argv['Op_Pharmacist_updateStock_run_8415']['date']
        state['TABLE_pharmacy_stock'].add({'stock_id': pharmacy_stock_stock_id}, {'drug_id': pharmacy_stock_drug_id,'brand_id': pharmacy_stock_brand_id,'stock': pharmacy_stock_stock,'remaining_quantity': pharmacy_stock_remaining_quantity,'manufac_date': pharmacy_stock_manufac_date,'exp_date': pharmacy_stock_exp_date,'supplier_id': pharmacy_stock_supplier_id,'date': pharmacy_stock_date})
        return state


class Op_Pharmacist_reduceStock_run_8416():
    def __init__(self):
        self.sops = [(self.cond0, self.csop0, self.sop0)]
        self.axiom = AxiomEmpty()

    def cond0(self, state, argv):
        id = argv['Op_Pharmacist_reduceStock_run_8416']['id']
        pharmacy_stock_stock_id = argv['Op_Pharmacist_reduceStock_run_8416']['pharmacy_stock_stock_id']
        return (state['TABLE_pharmacy_stock'].notNil({'stock_id': argv['Op_Pharmacist_reduceStock_run_8416']['id']}) == True)

    def csop0(self, state, argv):
        return True

    def sop0(self, state, argv):
        id = argv['Op_Pharmacist_reduceStock_run_8416']['id']
        pharmacy_stock_stock_id = argv['Op_Pharmacist_reduceStock_run_8416']['pharmacy_stock_stock_id']
        pharmacy_stock_stock_id = state['TABLE_pharmacy_stock'].get({'stock_id': argv['Op_Pharmacist_reduceStock_run_8416']['id']}, 'stock_id')
        pharmacy_stock_drug_id = state['TABLE_pharmacy_stock'].get({'stock_id': argv['Op_Pharmacist_reduceStock_run_8416']['id']}, 'drug_id')
        pharmacy_stock_brand_id = state['TABLE_pharmacy_stock'].get({'stock_id': argv['Op_Pharmacist_reduceStock_run_8416']['id']}, 'brand_id')
        pharmacy_stock_stock = state['TABLE_pharmacy_stock'].get({'stock_id': argv['Op_Pharmacist_reduceStock_run_8416']['id']}, 'stock')
        pharmacy_stock_remaining_quantity = state['TABLE_pharmacy_stock'].get({'stock_id': argv['Op_Pharmacist_reduceStock_run_8416']['id']}, 'remaining_quantity')
        pharmacy_stock_manufac_date = state['TABLE_pharmacy_stock'].get({'stock_id': argv['Op_Pharmacist_reduceStock_run_8416']['id']}, 'manufac_date')
        pharmacy_stock_exp_date = state['TABLE_pharmacy_stock'].get({'stock_id': argv['Op_Pharmacist_reduceStock_run_8416']['id']}, 'exp_date')
        pharmacy_stock_supplier_id = state['TABLE_pharmacy_stock'].get({'stock_id': argv['Op_Pharmacist_reduceStock_run_8416']['id']}, 'supplier_id')
        pharmacy_stock_date = state['TABLE_pharmacy_stock'].get({'stock_id': argv['Op_Pharmacist_reduceStock_run_8416']['id']}, 'date')
        pharmacy_stock_remaining_quantity = (pharmacy_stock_remaining_quantity)-(10)
        state['TABLE_pharmacy_stock'].update({'stock_id': argv['Op_Pharmacist_reduceStock_run_8416']['id']}, {'stock_id': pharmacy_stock_stock_id, 'drug_id': pharmacy_stock_drug_id, 'brand_id': pharmacy_stock_brand_id, 'stock': pharmacy_stock_stock, 'remaining_quantity': pharmacy_stock_remaining_quantity, 'manufac_date': pharmacy_stock_manufac_date, 'exp_date': pharmacy_stock_exp_date, 'supplier_id': pharmacy_stock_supplier_id, 'date': pharmacy_stock_date})
        return state


class Op_LabAssistant_updateLabAssistantInfo_run_8417():
    def __init__(self):
        self.sops = [(self.cond0, self.csop0, self.sop0)]
        self.axiom = AxiomEmpty()

    def cond0(self, state, argv):
        id = argv['Op_LabAssistant_updateLabAssistantInfo_run_8417']['id']
        lab_assistant_lab_assistant_id = argv['Op_LabAssistant_updateLabAssistantInfo_run_8417']['lab_assistant_lab_assistant_id']
        return (state['TABLE_lab_assistant'].notNil({'lab_assistant_id': argv['Op_LabAssistant_updateLabAssistantInfo_run_8417']['id']}) == True)

    def csop0(self, state, argv):
        return True

    def sop0(self, state, argv):
        id = argv['Op_LabAssistant_updateLabAssistantInfo_run_8417']['id']
        lab_assistant_lab_assistant_id = argv['Op_LabAssistant_updateLabAssistantInfo_run_8417']['lab_assistant_lab_assistant_id']
        lab_assistant_lab_assistant_id = state['TABLE_lab_assistant'].get({'lab_assistant_id': argv['Op_LabAssistant_updateLabAssistantInfo_run_8417']['id']}, 'lab_assistant_id')
        lab_assistant_user_id = state['TABLE_lab_assistant'].get({'lab_assistant_id': argv['Op_LabAssistant_updateLabAssistantInfo_run_8417']['id']}, 'user_id')
        lab_assistant_education = state['TABLE_lab_assistant'].get({'lab_assistant_id': argv['Op_LabAssistant_updateLabAssistantInfo_run_8417']['id']}, 'education')
        lab_assistant_training = state['TABLE_lab_assistant'].get({'lab_assistant_id': argv['Op_LabAssistant_updateLabAssistantInfo_run_8417']['id']}, 'training')
        lab_assistant_experience = state['TABLE_lab_assistant'].get({'lab_assistant_id': argv['Op_LabAssistant_updateLabAssistantInfo_run_8417']['id']}, 'experience')
        lab_assistant_achievements = state['TABLE_lab_assistant'].get({'lab_assistant_id': argv['Op_LabAssistant_updateLabAssistantInfo_run_8417']['id']}, 'achievements')
        lab_assistant_education = argv['Op_LabAssistant_updateLabAssistantInfo_run_8417']['id']
        state['TABLE_lab_assistant'].update({'lab_assistant_id': argv['Op_LabAssistant_updateLabAssistantInfo_run_8417']['id']}, {'lab_assistant_id': lab_assistant_lab_assistant_id, 'user_id': lab_assistant_user_id, 'education': lab_assistant_education, 'training': lab_assistant_training, 'experience': lab_assistant_experience, 'achievements': lab_assistant_achievements})
        return state


class Op_Receptionist_updateAccountInfo_run_8418():
    def __init__(self):
        self.sops = [(self.cond0, self.csop0, self.sop0)]
        self.axiom = AxiomEmpty()

    def cond0(self, state, argv):
        id = argv['Op_Receptionist_updateAccountInfo_run_8418']['id']
        doctor_user_id = argv['Op_Receptionist_updateAccountInfo_run_8418']['doctor_user_id']
        sys_user_user_id = argv['Op_Receptionist_updateAccountInfo_run_8418']['sys_user_user_id']
        return And((state['TABLE_doctor'].notNil({'slmc_reg_no': argv['Op_Receptionist_updateAccountInfo_run_8418']['id']}) == True),(state['TABLE_sys_user'].notNil({'user_id': state['TABLE_doctor'].get({'slmc_reg_no': argv['Op_Receptionist_updateAccountInfo_run_8418']['id']}, 'user_id')}) == True))

    def csop0(self, state, argv):
        return True

    def sop0(self, state, argv):
        id = argv['Op_Receptionist_updateAccountInfo_run_8418']['id']
        doctor_user_id = argv['Op_Receptionist_updateAccountInfo_run_8418']['doctor_user_id']
        sys_user_user_id = argv['Op_Receptionist_updateAccountInfo_run_8418']['sys_user_user_id']
        sys_user_person_id = state['TABLE_sys_user'].get({'user_id': state['TABLE_doctor'].get({'slmc_reg_no': argv['Op_Receptionist_updateAccountInfo_run_8418']['id']}, 'user_id')}, 'person_id')
        sys_user_user_id = state['TABLE_sys_user'].get({'user_id': state['TABLE_doctor'].get({'slmc_reg_no': argv['Op_Receptionist_updateAccountInfo_run_8418']['id']}, 'user_id')}, 'user_id')
        sys_user_user_name = state['TABLE_sys_user'].get({'user_id': state['TABLE_doctor'].get({'slmc_reg_no': argv['Op_Receptionist_updateAccountInfo_run_8418']['id']}, 'user_id')}, 'user_name')
        sys_user_user_type = state['TABLE_sys_user'].get({'user_id': state['TABLE_doctor'].get({'slmc_reg_no': argv['Op_Receptionist_updateAccountInfo_run_8418']['id']}, 'user_id')}, 'user_type')
        sys_user_other_info = state['TABLE_sys_user'].get({'user_id': state['TABLE_doctor'].get({'slmc_reg_no': argv['Op_Receptionist_updateAccountInfo_run_8418']['id']}, 'user_id')}, 'other_info')
        sys_user_password = state['TABLE_sys_user'].get({'user_id': state['TABLE_doctor'].get({'slmc_reg_no': argv['Op_Receptionist_updateAccountInfo_run_8418']['id']}, 'user_id')}, 'password')
        sys_user_online = state['TABLE_sys_user'].get({'user_id': state['TABLE_doctor'].get({'slmc_reg_no': argv['Op_Receptionist_updateAccountInfo_run_8418']['id']}, 'user_id')}, 'online')
        sys_user_login = state['TABLE_sys_user'].get({'user_id': state['TABLE_doctor'].get({'slmc_reg_no': argv['Op_Receptionist_updateAccountInfo_run_8418']['id']}, 'user_id')}, 'login')
        sys_user_logout = state['TABLE_sys_user'].get({'user_id': state['TABLE_doctor'].get({'slmc_reg_no': argv['Op_Receptionist_updateAccountInfo_run_8418']['id']}, 'user_id')}, 'logout')
        sys_user_profile_pic = state['TABLE_sys_user'].get({'user_id': state['TABLE_doctor'].get({'slmc_reg_no': argv['Op_Receptionist_updateAccountInfo_run_8418']['id']}, 'user_id')}, 'profile_pic')
        sys_user_suspend = state['TABLE_sys_user'].get({'user_id': state['TABLE_doctor'].get({'slmc_reg_no': argv['Op_Receptionist_updateAccountInfo_run_8418']['id']}, 'user_id')}, 'suspend')
        sys_user_other_info = argv['Op_Receptionist_updateAccountInfo_run_8418']['id']
        state['TABLE_sys_user'].update({'user_id': state['TABLE_doctor'].get({'slmc_reg_no': argv['Op_Receptionist_updateAccountInfo_run_8418']['id']}, 'user_id')}, {'person_id': sys_user_person_id, 'user_id': sys_user_user_id, 'user_name': sys_user_user_name, 'user_type': sys_user_user_type, 'other_info': sys_user_other_info, 'password': sys_user_password, 'online': sys_user_online, 'login': sys_user_login, 'logout': sys_user_logout, 'profile_pic': sys_user_profile_pic, 'suspend': sys_user_suspend})
        return state


class Op_Doctor_diagnose_run_8419():
    def __init__(self):
        self.sops = [(self.cond0, self.csop0, self.sop0)]
        self.axiom = AxiomEmpty()

    def cond0(self, state, argv):
        newHistoryId = argv['Op_Doctor_diagnose_run_8419']['newHistoryId']
        patientId = argv['Op_Doctor_diagnose_run_8419']['patientId']
        doctorId = argv['Op_Doctor_diagnose_run_8419']['doctorId']
        date = argv['Op_Doctor_diagnose_run_8419']['date']
        history = argv['Op_Doctor_diagnose_run_8419']['history']
        return (state['TABLE_medical_history'].notNil({'history_id': argv['Op_Doctor_diagnose_run_8419']['newHistoryId']}) == False)

    def csop0(self, state, argv):
        return True

    def sop0(self, state, argv):
        newHistoryId = argv['Op_Doctor_diagnose_run_8419']['newHistoryId']
        patientId = argv['Op_Doctor_diagnose_run_8419']['patientId']
        doctorId = argv['Op_Doctor_diagnose_run_8419']['doctorId']
        date = argv['Op_Doctor_diagnose_run_8419']['date']
        history = argv['Op_Doctor_diagnose_run_8419']['history']
        medical_history_history_id = argv['Op_Doctor_diagnose_run_8419']['newHistoryId']
        medical_history_patient_id = argv['Op_Doctor_diagnose_run_8419']['patientId']
        medical_history_doctor_id = argv['Op_Doctor_diagnose_run_8419']['doctorId']
        medical_history_date = 1451606400
        medical_history_history = StringVal('Took medicine for dengue fever')
        state['TABLE_medical_history'].add({'history_id': medical_history_history_id}, {'patient_id': medical_history_patient_id,'doctor_id': medical_history_doctor_id,'date': medical_history_date,'history': medical_history_history})
        return state


class Op_Pharmacist_updateAccountInfo_run_8420():
    def __init__(self):
        self.sops = [(self.cond0, self.csop0, self.sop0)]
        self.axiom = AxiomEmpty()

    def cond0(self, state, argv):
        pharmacistId = argv['Op_Pharmacist_updateAccountInfo_run_8420']['pharmacistId']
        pharmacist_user_id = argv['Op_Pharmacist_updateAccountInfo_run_8420']['pharmacist_user_id']
        sys_user_user_id = argv['Op_Pharmacist_updateAccountInfo_run_8420']['sys_user_user_id']
        return And((state['TABLE_pharmacist'].notNil({'pharmacist_id': argv['Op_Pharmacist_updateAccountInfo_run_8420']['pharmacistId']}) == True),(state['TABLE_sys_user'].notNil({'user_id': state['TABLE_pharmacist'].get({'pharmacist_id': argv['Op_Pharmacist_updateAccountInfo_run_8420']['pharmacistId']}, 'user_id')}) == True))

    def csop0(self, state, argv):
        return True

    def sop0(self, state, argv):
        pharmacistId = argv['Op_Pharmacist_updateAccountInfo_run_8420']['pharmacistId']
        pharmacist_user_id = argv['Op_Pharmacist_updateAccountInfo_run_8420']['pharmacist_user_id']
        sys_user_user_id = argv['Op_Pharmacist_updateAccountInfo_run_8420']['sys_user_user_id']
        sys_user_person_id = state['TABLE_sys_user'].get({'user_id': state['TABLE_pharmacist'].get({'pharmacist_id': argv['Op_Pharmacist_updateAccountInfo_run_8420']['pharmacistId']}, 'user_id')}, 'person_id')
        sys_user_user_id = state['TABLE_sys_user'].get({'user_id': state['TABLE_pharmacist'].get({'pharmacist_id': argv['Op_Pharmacist_updateAccountInfo_run_8420']['pharmacistId']}, 'user_id')}, 'user_id')
        sys_user_user_name = state['TABLE_sys_user'].get({'user_id': state['TABLE_pharmacist'].get({'pharmacist_id': argv['Op_Pharmacist_updateAccountInfo_run_8420']['pharmacistId']}, 'user_id')}, 'user_name')
        sys_user_user_type = state['TABLE_sys_user'].get({'user_id': state['TABLE_pharmacist'].get({'pharmacist_id': argv['Op_Pharmacist_updateAccountInfo_run_8420']['pharmacistId']}, 'user_id')}, 'user_type')
        sys_user_other_info = state['TABLE_sys_user'].get({'user_id': state['TABLE_pharmacist'].get({'pharmacist_id': argv['Op_Pharmacist_updateAccountInfo_run_8420']['pharmacistId']}, 'user_id')}, 'other_info')
        sys_user_password = state['TABLE_sys_user'].get({'user_id': state['TABLE_pharmacist'].get({'pharmacist_id': argv['Op_Pharmacist_updateAccountInfo_run_8420']['pharmacistId']}, 'user_id')}, 'password')
        sys_user_online = state['TABLE_sys_user'].get({'user_id': state['TABLE_pharmacist'].get({'pharmacist_id': argv['Op_Pharmacist_updateAccountInfo_run_8420']['pharmacistId']}, 'user_id')}, 'online')
        sys_user_login = state['TABLE_sys_user'].get({'user_id': state['TABLE_pharmacist'].get({'pharmacist_id': argv['Op_Pharmacist_updateAccountInfo_run_8420']['pharmacistId']}, 'user_id')}, 'login')
        sys_user_logout = state['TABLE_sys_user'].get({'user_id': state['TABLE_pharmacist'].get({'pharmacist_id': argv['Op_Pharmacist_updateAccountInfo_run_8420']['pharmacistId']}, 'user_id')}, 'logout')
        sys_user_profile_pic = state['TABLE_sys_user'].get({'user_id': state['TABLE_pharmacist'].get({'pharmacist_id': argv['Op_Pharmacist_updateAccountInfo_run_8420']['pharmacistId']}, 'user_id')}, 'profile_pic')
        sys_user_suspend = state['TABLE_sys_user'].get({'user_id': state['TABLE_pharmacist'].get({'pharmacist_id': argv['Op_Pharmacist_updateAccountInfo_run_8420']['pharmacistId']}, 'user_id')}, 'suspend')
        sys_user_other_info = argv['Op_Pharmacist_updateAccountInfo_run_8420']['pharmacistId']
        state['TABLE_sys_user'].update({'user_id': state['TABLE_pharmacist'].get({'pharmacist_id': argv['Op_Pharmacist_updateAccountInfo_run_8420']['pharmacistId']}, 'user_id')}, {'person_id': sys_user_person_id, 'user_id': sys_user_user_id, 'user_name': sys_user_user_name, 'user_type': sys_user_user_type, 'other_info': sys_user_other_info, 'password': sys_user_password, 'online': sys_user_online, 'login': sys_user_login, 'logout': sys_user_logout, 'profile_pic': sys_user_profile_pic, 'suspend': sys_user_suspend})
        return state


class Op_LabAssistant_UrineFullReport_run_8421():
    def __init__(self):
        self.sops = [(self.cond0, self.csop0, self.sop0)]
        self.axiom = AxiomEmpty()

    def cond0(self, state, argv):
        newTstId = argv['Op_LabAssistant_UrineFullReport_run_8421']['newTstId']
        appId = argv['Op_LabAssistant_UrineFullReport_run_8421']['appId']
        appearance = argv['Op_LabAssistant_UrineFullReport_run_8421']['appearance']
        sgRefractometer = argv['Op_LabAssistant_UrineFullReport_run_8421']['sgRefractometer']
        ph = argv['Op_LabAssistant_UrineFullReport_run_8421']['ph']
        protein = argv['Op_LabAssistant_UrineFullReport_run_8421']['protein']
        glucose = argv['Op_LabAssistant_UrineFullReport_run_8421']['glucose']
        ketoneBodies = argv['Op_LabAssistant_UrineFullReport_run_8421']['ketoneBodies']
        bilirubin = argv['Op_LabAssistant_UrineFullReport_run_8421']['bilirubin']
        urobilirubin = argv['Op_LabAssistant_UrineFullReport_run_8421']['urobilirubin']
        contrifugedDepositsphaseContrastMicroscopy = argv['Op_LabAssistant_UrineFullReport_run_8421']['contrifugedDepositsphaseContrastMicroscopy']
        pusCells = argv['Op_LabAssistant_UrineFullReport_run_8421']['pusCells']
        redCells = argv['Op_LabAssistant_UrineFullReport_run_8421']['redCells']
        epithelialCells = argv['Op_LabAssistant_UrineFullReport_run_8421']['epithelialCells']
        casts = argv['Op_LabAssistant_UrineFullReport_run_8421']['casts']
        cristals = argv['Op_LabAssistant_UrineFullReport_run_8421']['cristals']
        now = argv['Op_LabAssistant_UrineFullReport_run_8421']['now']
        return (state['TABLE_UrineFullReport'].notNil({'tst_ur_id': argv['Op_LabAssistant_UrineFullReport_run_8421']['newTstId']}) == False)

    def csop0(self, state, argv):
        return True

    def sop0(self, state, argv):
        newTstId = argv['Op_LabAssistant_UrineFullReport_run_8421']['newTstId']
        appId = argv['Op_LabAssistant_UrineFullReport_run_8421']['appId']
        appearance = argv['Op_LabAssistant_UrineFullReport_run_8421']['appearance']
        sgRefractometer = argv['Op_LabAssistant_UrineFullReport_run_8421']['sgRefractometer']
        ph = argv['Op_LabAssistant_UrineFullReport_run_8421']['ph']
        protein = argv['Op_LabAssistant_UrineFullReport_run_8421']['protein']
        glucose = argv['Op_LabAssistant_UrineFullReport_run_8421']['glucose']
        ketoneBodies = argv['Op_LabAssistant_UrineFullReport_run_8421']['ketoneBodies']
        bilirubin = argv['Op_LabAssistant_UrineFullReport_run_8421']['bilirubin']
        urobilirubin = argv['Op_LabAssistant_UrineFullReport_run_8421']['urobilirubin']
        contrifugedDepositsphaseContrastMicroscopy = argv['Op_LabAssistant_UrineFullReport_run_8421']['contrifugedDepositsphaseContrastMicroscopy']
        pusCells = argv['Op_LabAssistant_UrineFullReport_run_8421']['pusCells']
        redCells = argv['Op_LabAssistant_UrineFullReport_run_8421']['redCells']
        epithelialCells = argv['Op_LabAssistant_UrineFullReport_run_8421']['epithelialCells']
        casts = argv['Op_LabAssistant_UrineFullReport_run_8421']['casts']
        cristals = argv['Op_LabAssistant_UrineFullReport_run_8421']['cristals']
        now = argv['Op_LabAssistant_UrineFullReport_run_8421']['now']
        UrineFullReport_tst_ur_id = argv['Op_LabAssistant_UrineFullReport_run_8421']['newTstId']
        UrineFullReport_appointment_id = argv['Op_LabAssistant_UrineFullReport_run_8421']['appId']
        UrineFullReport_appearance = argv['Op_LabAssistant_UrineFullReport_run_8421']['appearance']
        UrineFullReport_sgRefractometer = argv['Op_LabAssistant_UrineFullReport_run_8421']['sgRefractometer']
        UrineFullReport_ph = argv['Op_LabAssistant_UrineFullReport_run_8421']['ph']
        UrineFullReport_protein = argv['Op_LabAssistant_UrineFullReport_run_8421']['protein']
        UrineFullReport_glucose = argv['Op_LabAssistant_UrineFullReport_run_8421']['glucose']
        UrineFullReport_ketoneBodies = argv['Op_LabAssistant_UrineFullReport_run_8421']['ketoneBodies']
        UrineFullReport_bilirubin = argv['Op_LabAssistant_UrineFullReport_run_8421']['bilirubin']
        UrineFullReport_urobilirubin = argv['Op_LabAssistant_UrineFullReport_run_8421']['urobilirubin']
        UrineFullReport_contrifugedDepositsphaseContrastMicroscopy = argv['Op_LabAssistant_UrineFullReport_run_8421']['contrifugedDepositsphaseContrastMicroscopy']
        UrineFullReport_pusCells = argv['Op_LabAssistant_UrineFullReport_run_8421']['pusCells']
        UrineFullReport_redCells = argv['Op_LabAssistant_UrineFullReport_run_8421']['redCells']
        UrineFullReport_epithelialCells = argv['Op_LabAssistant_UrineFullReport_run_8421']['epithelialCells']
        UrineFullReport_casts = argv['Op_LabAssistant_UrineFullReport_run_8421']['casts']
        UrineFullReport_cristals = argv['Op_LabAssistant_UrineFullReport_run_8421']['cristals']
        UrineFullReport_date = argv['Op_LabAssistant_UrineFullReport_run_8421']['now']
        state['TABLE_UrineFullReport'].add({'tst_ur_id': UrineFullReport_tst_ur_id}, {'appointment_id': UrineFullReport_appointment_id,'appearance': UrineFullReport_appearance,'sgRefractometer': UrineFullReport_sgRefractometer,'ph': UrineFullReport_ph,'protein': UrineFullReport_protein,'glucose': UrineFullReport_glucose,'ketoneBodies': UrineFullReport_ketoneBodies,'bilirubin': UrineFullReport_bilirubin,'urobilirubin': UrineFullReport_urobilirubin,'contrifugedDepositsphaseContrastMicroscopy': UrineFullReport_contrifugedDepositsphaseContrastMicroscopy,'pusCells': UrineFullReport_pusCells,'redCells': UrineFullReport_redCells,'epithelialCells': UrineFullReport_epithelialCells,'casts': UrineFullReport_casts,'cristals': UrineFullReport_cristals,'date': UrineFullReport_date})
        return state


class Op_Receptionist_cancelAppointment_run_8422():
    def __init__(self):
        self.sops = [(self.cond0, self.csop0, self.sop0), (self.cond1, self.csop1, self.sop1), (self.cond2, self.csop2, self.sop2)]
        self.axiom = AxiomEmpty()

    def cond0(self, state, argv):
        appointmentId = argv['Op_Receptionist_cancelAppointment_run_8422']['appointmentId']
        appointment_appointment_id = argv['Op_Receptionist_cancelAppointment_run_8422']['appointment_appointment_id']
        appointmentId = argv['Op_Receptionist_cancelAppointment_run_8422']['appointmentId']
        appointment_appointment_id = argv['Op_Receptionist_cancelAppointment_run_8422']['appointment_appointment_id']
        appointment_bill_id = argv['Op_Receptionist_cancelAppointment_run_8422']['appointment_bill_id']
        newRefundId = argv['Op_Receptionist_cancelAppointment_run_8422']['newRefundId']
        bill_total = argv['Op_Receptionist_cancelAppointment_run_8422']['bill_total']
        now = argv['Op_Receptionist_cancelAppointment_run_8422']['now']
        appointmentId = argv['Op_Receptionist_cancelAppointment_run_8422']['appointmentId']
        appointment_appointment_id = argv['Op_Receptionist_cancelAppointment_run_8422']['appointment_appointment_id']
        appointment_bill_id = argv['Op_Receptionist_cancelAppointment_run_8422']['appointment_bill_id']
        newRefundId = argv['Op_Receptionist_cancelAppointment_run_8422']['newRefundId']
        bill_total = argv['Op_Receptionist_cancelAppointment_run_8422']['bill_total']
        now = argv['Op_Receptionist_cancelAppointment_run_8422']['now']
        bill_bill_id = argv['Op_Receptionist_cancelAppointment_run_8422']['bill_bill_id']
        return And((state['TABLE_appointment'].notNil({'appointment_id': argv['Op_Receptionist_cancelAppointment_run_8422']['appointmentId']}) == True),Not((state['TABLE_appointment'].notNil({'appointment_id': argv['Op_Receptionist_cancelAppointment_run_8422']['appointmentId']}) == True)),Not((state['TABLE_appointment'].notNil({'appointment_id': argv['Op_Receptionist_cancelAppointment_run_8422']['appointmentId']}) == True)),Not((state['TABLE_bill'].notNil({'bill_id': state['TABLE_appointment'].get({'appointment_id': argv['Op_Receptionist_cancelAppointment_run_8422']['appointmentId']}, 'bill_id')}) == True)),Not((state['TABLE_appointment'].notNil({'appointment_id': argv['Op_Receptionist_cancelAppointment_run_8422']['appointmentId']}) == True)),Not((state['TABLE_appointment'].notNil({'appointment_id': argv['Op_Receptionist_cancelAppointment_run_8422']['appointmentId']}) == True)),Not((state['TABLE_bill'].notNil({'bill_id': state['TABLE_appointment'].get({'appointment_id': argv['Op_Receptionist_cancelAppointment_run_8422']['appointmentId']}, 'bill_id')}) == True)),Not((state['TABLE_bill'].notNil({'bill_id': state['TABLE_appointment'].get({'appointment_id': argv['Op_Receptionist_cancelAppointment_run_8422']['appointmentId']}, 'bill_id')}) == True)))

    def csop0(self, state, argv):
        return True

    def sop0(self, state, argv):
        appointmentId = argv['Op_Receptionist_cancelAppointment_run_8422']['appointmentId']
        appointment_appointment_id = argv['Op_Receptionist_cancelAppointment_run_8422']['appointment_appointment_id']
        appointment_appointment_id = state['TABLE_appointment'].get({'appointment_id': argv['Op_Receptionist_cancelAppointment_run_8422']['appointmentId']}, 'appointment_id')
        appointment_date = state['TABLE_appointment'].get({'appointment_id': argv['Op_Receptionist_cancelAppointment_run_8422']['appointmentId']}, 'date')
        appointment_info = state['TABLE_appointment'].get({'appointment_id': argv['Op_Receptionist_cancelAppointment_run_8422']['appointmentId']}, 'info')
        appointment_patient_id = state['TABLE_appointment'].get({'appointment_id': argv['Op_Receptionist_cancelAppointment_run_8422']['appointmentId']}, 'patient_id')
        appointment_bill_id = state['TABLE_appointment'].get({'appointment_id': argv['Op_Receptionist_cancelAppointment_run_8422']['appointmentId']}, 'bill_id')
        appointment_slmc_reg_no = state['TABLE_appointment'].get({'appointment_id': argv['Op_Receptionist_cancelAppointment_run_8422']['appointmentId']}, 'slmc_reg_no')
        appointment_cancelled = state['TABLE_appointment'].get({'appointment_id': argv['Op_Receptionist_cancelAppointment_run_8422']['appointmentId']}, 'cancelled')
        appointment_cancelled = True
        state['TABLE_appointment'].update({'appointment_id': argv['Op_Receptionist_cancelAppointment_run_8422']['appointmentId']}, {'appointment_id': appointment_appointment_id, 'date': appointment_date, 'info': appointment_info, 'patient_id': appointment_patient_id, 'bill_id': appointment_bill_id, 'slmc_reg_no': appointment_slmc_reg_no, 'cancelled': appointment_cancelled})
        return state

    def cond1(self, state, argv):
        appointmentId = argv['Op_Receptionist_cancelAppointment_run_8422']['appointmentId']
        appointment_appointment_id = argv['Op_Receptionist_cancelAppointment_run_8422']['appointment_appointment_id']
        appointment_bill_id = argv['Op_Receptionist_cancelAppointment_run_8422']['appointment_bill_id']
        newRefundId = argv['Op_Receptionist_cancelAppointment_run_8422']['newRefundId']
        bill_total = argv['Op_Receptionist_cancelAppointment_run_8422']['bill_total']
        now = argv['Op_Receptionist_cancelAppointment_run_8422']['now']
        appointmentId = argv['Op_Receptionist_cancelAppointment_run_8422']['appointmentId']
        appointment_appointment_id = argv['Op_Receptionist_cancelAppointment_run_8422']['appointment_appointment_id']
        appointment_bill_id = argv['Op_Receptionist_cancelAppointment_run_8422']['appointment_bill_id']
        newRefundId = argv['Op_Receptionist_cancelAppointment_run_8422']['newRefundId']
        bill_total = argv['Op_Receptionist_cancelAppointment_run_8422']['bill_total']
        now = argv['Op_Receptionist_cancelAppointment_run_8422']['now']
        bill_bill_id = argv['Op_Receptionist_cancelAppointment_run_8422']['bill_bill_id']
        return And((state['TABLE_appointment'].notNil({'appointment_id': argv['Op_Receptionist_cancelAppointment_run_8422']['appointmentId']}) == True),(state['TABLE_appointment'].notNil({'appointment_id': argv['Op_Receptionist_cancelAppointment_run_8422']['appointmentId']}) == True),(state['TABLE_bill'].notNil({'bill_id': state['TABLE_appointment'].get({'appointment_id': argv['Op_Receptionist_cancelAppointment_run_8422']['appointmentId']}, 'bill_id')}) == True),Not((state['TABLE_appointment'].notNil({'appointment_id': argv['Op_Receptionist_cancelAppointment_run_8422']['appointmentId']}) == True)),Not((state['TABLE_appointment'].notNil({'appointment_id': argv['Op_Receptionist_cancelAppointment_run_8422']['appointmentId']}) == True)),Not((state['TABLE_bill'].notNil({'bill_id': state['TABLE_appointment'].get({'appointment_id': argv['Op_Receptionist_cancelAppointment_run_8422']['appointmentId']}, 'bill_id')}) == True)),Not((state['TABLE_bill'].notNil({'bill_id': state['TABLE_appointment'].get({'appointment_id': argv['Op_Receptionist_cancelAppointment_run_8422']['appointmentId']}, 'bill_id')}) == True)))

    def csop1(self, state, argv):
        return True

    def sop1(self, state, argv):
        appointmentId = argv['Op_Receptionist_cancelAppointment_run_8422']['appointmentId']
        appointment_appointment_id = argv['Op_Receptionist_cancelAppointment_run_8422']['appointment_appointment_id']
        appointment_bill_id = argv['Op_Receptionist_cancelAppointment_run_8422']['appointment_bill_id']
        newRefundId = argv['Op_Receptionist_cancelAppointment_run_8422']['newRefundId']
        bill_total = argv['Op_Receptionist_cancelAppointment_run_8422']['bill_total']
        now = argv['Op_Receptionist_cancelAppointment_run_8422']['now']
        appointment_appointment_id = state['TABLE_appointment'].get({'appointment_id': argv['Op_Receptionist_cancelAppointment_run_8422']['appointmentId']}, 'appointment_id')
        appointment_date = state['TABLE_appointment'].get({'appointment_id': argv['Op_Receptionist_cancelAppointment_run_8422']['appointmentId']}, 'date')
        appointment_info = state['TABLE_appointment'].get({'appointment_id': argv['Op_Receptionist_cancelAppointment_run_8422']['appointmentId']}, 'info')
        appointment_patient_id = state['TABLE_appointment'].get({'appointment_id': argv['Op_Receptionist_cancelAppointment_run_8422']['appointmentId']}, 'patient_id')
        appointment_bill_id = state['TABLE_appointment'].get({'appointment_id': argv['Op_Receptionist_cancelAppointment_run_8422']['appointmentId']}, 'bill_id')
        appointment_slmc_reg_no = state['TABLE_appointment'].get({'appointment_id': argv['Op_Receptionist_cancelAppointment_run_8422']['appointmentId']}, 'slmc_reg_no')
        appointment_cancelled = state['TABLE_appointment'].get({'appointment_id': argv['Op_Receptionist_cancelAppointment_run_8422']['appointmentId']}, 'cancelled')
        appointment_cancelled = True
        state['TABLE_appointment'].update({'appointment_id': argv['Op_Receptionist_cancelAppointment_run_8422']['appointmentId']}, {'appointment_id': appointment_appointment_id, 'date': appointment_date, 'info': appointment_info, 'patient_id': appointment_patient_id, 'bill_id': appointment_bill_id, 'slmc_reg_no': appointment_slmc_reg_no, 'cancelled': appointment_cancelled})
        refund_refund_id = argv['Op_Receptionist_cancelAppointment_run_8422']['newRefundId']
        refund_bill_id = state['TABLE_appointment'].get({'appointment_id': argv['Op_Receptionist_cancelAppointment_run_8422']['appointmentId']}, 'bill_id')
        refund_payment_type = StringVal('docApp')
        refund_reason = StringVal('no_reason')
        refund_amount = state['TABLE_bill'].get({'bill_id': state['TABLE_appointment'].get({'appointment_id': argv['Op_Receptionist_cancelAppointment_run_8422']['appointmentId']}, 'bill_id')}, 'total')
        refund_date = argv['Op_Receptionist_cancelAppointment_run_8422']['now']
        state['TABLE_refund'].add({'refund_id': refund_refund_id}, {'bill_id': refund_bill_id,'payment_type': refund_payment_type,'reason': refund_reason,'amount': refund_amount,'date': refund_date})
        return state

    def cond2(self, state, argv):
        appointmentId = argv['Op_Receptionist_cancelAppointment_run_8422']['appointmentId']
        appointment_appointment_id = argv['Op_Receptionist_cancelAppointment_run_8422']['appointment_appointment_id']
        appointment_bill_id = argv['Op_Receptionist_cancelAppointment_run_8422']['appointment_bill_id']
        newRefundId = argv['Op_Receptionist_cancelAppointment_run_8422']['newRefundId']
        bill_total = argv['Op_Receptionist_cancelAppointment_run_8422']['bill_total']
        now = argv['Op_Receptionist_cancelAppointment_run_8422']['now']
        bill_bill_id = argv['Op_Receptionist_cancelAppointment_run_8422']['bill_bill_id']
        return And((state['TABLE_appointment'].notNil({'appointment_id': argv['Op_Receptionist_cancelAppointment_run_8422']['appointmentId']}) == True),(state['TABLE_appointment'].notNil({'appointment_id': argv['Op_Receptionist_cancelAppointment_run_8422']['appointmentId']}) == True),(state['TABLE_bill'].notNil({'bill_id': state['TABLE_appointment'].get({'appointment_id': argv['Op_Receptionist_cancelAppointment_run_8422']['appointmentId']}, 'bill_id')}) == True),(state['TABLE_bill'].notNil({'bill_id': state['TABLE_appointment'].get({'appointment_id': argv['Op_Receptionist_cancelAppointment_run_8422']['appointmentId']}, 'bill_id')}) == True))

    def csop2(self, state, argv):
        return True

    def sop2(self, state, argv):
        appointmentId = argv['Op_Receptionist_cancelAppointment_run_8422']['appointmentId']
        appointment_appointment_id = argv['Op_Receptionist_cancelAppointment_run_8422']['appointment_appointment_id']
        appointment_bill_id = argv['Op_Receptionist_cancelAppointment_run_8422']['appointment_bill_id']
        newRefundId = argv['Op_Receptionist_cancelAppointment_run_8422']['newRefundId']
        bill_total = argv['Op_Receptionist_cancelAppointment_run_8422']['bill_total']
        now = argv['Op_Receptionist_cancelAppointment_run_8422']['now']
        bill_bill_id = argv['Op_Receptionist_cancelAppointment_run_8422']['bill_bill_id']
        appointment_appointment_id = state['TABLE_appointment'].get({'appointment_id': argv['Op_Receptionist_cancelAppointment_run_8422']['appointmentId']}, 'appointment_id')
        appointment_date = state['TABLE_appointment'].get({'appointment_id': argv['Op_Receptionist_cancelAppointment_run_8422']['appointmentId']}, 'date')
        appointment_info = state['TABLE_appointment'].get({'appointment_id': argv['Op_Receptionist_cancelAppointment_run_8422']['appointmentId']}, 'info')
        appointment_patient_id = state['TABLE_appointment'].get({'appointment_id': argv['Op_Receptionist_cancelAppointment_run_8422']['appointmentId']}, 'patient_id')
        appointment_bill_id = state['TABLE_appointment'].get({'appointment_id': argv['Op_Receptionist_cancelAppointment_run_8422']['appointmentId']}, 'bill_id')
        appointment_slmc_reg_no = state['TABLE_appointment'].get({'appointment_id': argv['Op_Receptionist_cancelAppointment_run_8422']['appointmentId']}, 'slmc_reg_no')
        appointment_cancelled = state['TABLE_appointment'].get({'appointment_id': argv['Op_Receptionist_cancelAppointment_run_8422']['appointmentId']}, 'cancelled')
        appointment_cancelled = True
        state['TABLE_appointment'].update({'appointment_id': argv['Op_Receptionist_cancelAppointment_run_8422']['appointmentId']}, {'appointment_id': appointment_appointment_id, 'date': appointment_date, 'info': appointment_info, 'patient_id': appointment_patient_id, 'bill_id': appointment_bill_id, 'slmc_reg_no': appointment_slmc_reg_no, 'cancelled': appointment_cancelled})
        refund_refund_id = argv['Op_Receptionist_cancelAppointment_run_8422']['newRefundId']
        refund_bill_id = state['TABLE_appointment'].get({'appointment_id': argv['Op_Receptionist_cancelAppointment_run_8422']['appointmentId']}, 'bill_id')
        refund_payment_type = StringVal('docApp')
        refund_reason = StringVal('no_reason')
        refund_amount = state['TABLE_bill'].get({'bill_id': state['TABLE_appointment'].get({'appointment_id': argv['Op_Receptionist_cancelAppointment_run_8422']['appointmentId']}, 'bill_id')}, 'total')
        refund_date = argv['Op_Receptionist_cancelAppointment_run_8422']['now']
        state['TABLE_refund'].add({'refund_id': refund_refund_id}, {'bill_id': refund_bill_id,'payment_type': refund_payment_type,'reason': refund_reason,'amount': refund_amount,'date': refund_date})
        bill_bill_id = state['TABLE_bill'].get({'bill_id': state['TABLE_appointment'].get({'appointment_id': argv['Op_Receptionist_cancelAppointment_run_8422']['appointmentId']}, 'bill_id')}, 'bill_id')
        bill_bill_date = state['TABLE_bill'].get({'bill_id': state['TABLE_appointment'].get({'appointment_id': argv['Op_Receptionist_cancelAppointment_run_8422']['appointmentId']}, 'bill_id')}, 'bill_date')
        bill_doctor_fee = state['TABLE_bill'].get({'bill_id': state['TABLE_appointment'].get({'appointment_id': argv['Op_Receptionist_cancelAppointment_run_8422']['appointmentId']}, 'bill_id')}, 'doctor_fee')
        bill_hospital_fee = state['TABLE_bill'].get({'bill_id': state['TABLE_appointment'].get({'appointment_id': argv['Op_Receptionist_cancelAppointment_run_8422']['appointmentId']}, 'bill_id')}, 'hospital_fee')
        bill_pharmacy_fee = state['TABLE_bill'].get({'bill_id': state['TABLE_appointment'].get({'appointment_id': argv['Op_Receptionist_cancelAppointment_run_8422']['appointmentId']}, 'bill_id')}, 'pharmacy_fee')
        bill_laboratory_fee = state['TABLE_bill'].get({'bill_id': state['TABLE_appointment'].get({'appointment_id': argv['Op_Receptionist_cancelAppointment_run_8422']['appointmentId']}, 'bill_id')}, 'laboratory_fee')
        bill_appointment_fee = state['TABLE_bill'].get({'bill_id': state['TABLE_appointment'].get({'appointment_id': argv['Op_Receptionist_cancelAppointment_run_8422']['appointmentId']}, 'bill_id')}, 'appointment_fee')
        bill_vat = state['TABLE_bill'].get({'bill_id': state['TABLE_appointment'].get({'appointment_id': argv['Op_Receptionist_cancelAppointment_run_8422']['appointmentId']}, 'bill_id')}, 'vat')
        bill_discount = state['TABLE_bill'].get({'bill_id': state['TABLE_appointment'].get({'appointment_id': argv['Op_Receptionist_cancelAppointment_run_8422']['appointmentId']}, 'bill_id')}, 'discount')
        bill_total = state['TABLE_bill'].get({'bill_id': state['TABLE_appointment'].get({'appointment_id': argv['Op_Receptionist_cancelAppointment_run_8422']['appointmentId']}, 'bill_id')}, 'total')
        bill_payment_method = state['TABLE_bill'].get({'bill_id': state['TABLE_appointment'].get({'appointment_id': argv['Op_Receptionist_cancelAppointment_run_8422']['appointmentId']}, 'bill_id')}, 'payment_method')
        bill_consultant_id = state['TABLE_bill'].get({'bill_id': state['TABLE_appointment'].get({'appointment_id': argv['Op_Receptionist_cancelAppointment_run_8422']['appointmentId']}, 'bill_id')}, 'consultant_id')
        bill_patient_id = state['TABLE_bill'].get({'bill_id': state['TABLE_appointment'].get({'appointment_id': argv['Op_Receptionist_cancelAppointment_run_8422']['appointmentId']}, 'bill_id')}, 'patient_id')
        bill_refund = state['TABLE_bill'].get({'bill_id': state['TABLE_appointment'].get({'appointment_id': argv['Op_Receptionist_cancelAppointment_run_8422']['appointmentId']}, 'bill_id')}, 'refund')
        bill_refund = 1
        state['TABLE_bill'].update({'bill_id': state['TABLE_appointment'].get({'appointment_id': argv['Op_Receptionist_cancelAppointment_run_8422']['appointmentId']}, 'bill_id')}, {'bill_id': bill_bill_id, 'bill_date': bill_bill_date, 'doctor_fee': bill_doctor_fee, 'hospital_fee': bill_hospital_fee, 'pharmacy_fee': bill_pharmacy_fee, 'laboratory_fee': bill_laboratory_fee, 'appointment_fee': bill_appointment_fee, 'vat': bill_vat, 'discount': bill_discount, 'total': bill_total, 'payment_method': bill_payment_method, 'consultant_id': bill_consultant_id, 'patient_id': bill_patient_id, 'refund': bill_refund})
        return state


class Op_Cashier_makeRefund_run_8423():
    def __init__(self):
        self.sops = [(self.cond0, self.csop0, self.sop0)]
        self.axiom = AxiomEmpty()

    def cond0(self, state, argv):
        id = argv['Op_Cashier_makeRefund_run_8423']['id']
        return True

    def csop0(self, state, argv):
        return True

    def sop0(self, state, argv):
        id = argv['Op_Cashier_makeRefund_run_8423']['id']
        state['TABLE_refund'].delete({'refund_id': argv['Op_Cashier_makeRefund_run_8423']['id']})
        return state


class Op_Cashier_refund_run_8424():
    def __init__(self):
        self.sops = [(self.cond0, self.csop0, self.sop0)]
        self.axiom = AxiomEmpty()

    def cond0(self, state, argv):
        newRefundId = argv['Op_Cashier_refund_run_8424']['newRefundId']
        billId = argv['Op_Cashier_refund_run_8424']['billId']
        paymentType = argv['Op_Cashier_refund_run_8424']['paymentType']
        reason = argv['Op_Cashier_refund_run_8424']['reason']
        amount = argv['Op_Cashier_refund_run_8424']['amount']
        now = argv['Op_Cashier_refund_run_8424']['now']
        return (state['TABLE_refund'].notNil({'refund_id': argv['Op_Cashier_refund_run_8424']['newRefundId']}) == False)

    def csop0(self, state, argv):
        return True

    def sop0(self, state, argv):
        newRefundId = argv['Op_Cashier_refund_run_8424']['newRefundId']
        billId = argv['Op_Cashier_refund_run_8424']['billId']
        paymentType = argv['Op_Cashier_refund_run_8424']['paymentType']
        reason = argv['Op_Cashier_refund_run_8424']['reason']
        amount = argv['Op_Cashier_refund_run_8424']['amount']
        now = argv['Op_Cashier_refund_run_8424']['now']
        refund_refund_id = argv['Op_Cashier_refund_run_8424']['newRefundId']
        refund_bill_id = argv['Op_Cashier_refund_run_8424']['billId']
        refund_payment_type = argv['Op_Cashier_refund_run_8424']['paymentType']
        refund_reason = argv['Op_Cashier_refund_run_8424']['reason']
        refund_amount = argv['Op_Cashier_refund_run_8424']['amount']
        refund_date = argv['Op_Cashier_refund_run_8424']['now']
        state['TABLE_refund'].add({'refund_id': refund_refund_id}, {'bill_id': refund_bill_id,'payment_type': refund_payment_type,'reason': refund_reason,'amount': refund_amount,'date': refund_date})
        return state


class Op_Doctor_allergies_run_8425():
    def __init__(self):
        self.sops = [(self.cond0, self.csop0, self.sop0)]
        self.axiom = AxiomEmpty()

    def cond0(self, state, argv):
        patientId = argv['Op_Doctor_allergies_run_8425']['patientId']
        patient_drug_allergies_and_reactions = argv['Op_Doctor_allergies_run_8425']['patient_drug_allergies_and_reactions']
        allergies = argv['Op_Doctor_allergies_run_8425']['allergies']
        patient_patient_id = argv['Op_Doctor_allergies_run_8425']['patient_patient_id']
        return And((state['TABLE_patient'].notNil({'patient_id': argv['Op_Doctor_allergies_run_8425']['patientId']}) == True),(state['TABLE_patient'].notNil({'patient_id': argv['Op_Doctor_allergies_run_8425']['patientId']}) == True))

    def csop0(self, state, argv):
        return True

    def sop0(self, state, argv):
        patientId = argv['Op_Doctor_allergies_run_8425']['patientId']
        patient_drug_allergies_and_reactions = argv['Op_Doctor_allergies_run_8425']['patient_drug_allergies_and_reactions']
        allergies = argv['Op_Doctor_allergies_run_8425']['allergies']
        patient_patient_id = argv['Op_Doctor_allergies_run_8425']['patient_patient_id']
        patient_patient_id = state['TABLE_patient'].get({'patient_id': argv['Op_Doctor_allergies_run_8425']['patientId']}, 'patient_id')
        patient_person_id = state['TABLE_patient'].get({'patient_id': argv['Op_Doctor_allergies_run_8425']['patientId']}, 'person_id')
        patient_drug_allergies_and_reactions = state['TABLE_patient'].get({'patient_id': argv['Op_Doctor_allergies_run_8425']['patientId']}, 'drug_allergies_and_reactions')
        patient_drug_allergies_and_reactions = ((state['TABLE_patient'].get({'patient_id': argv['Op_Doctor_allergies_run_8425']['patientId']}, 'drug_allergies_and_reactions'))+(StringVal(',')))+(argv['Op_Doctor_allergies_run_8425']['allergies'])
        state['TABLE_patient'].update({'patient_id': argv['Op_Doctor_allergies_run_8425']['patientId']}, {'patient_id': patient_patient_id, 'person_id': patient_person_id, 'drug_allergies_and_reactions': patient_drug_allergies_and_reactions})
        return state


class Op_Admin_createNewUser_run_8426():
    def __init__(self):
        self.sops = [(self.cond0, self.csop0, self.sop0), (self.cond1, self.csop1, self.sop1), (self.cond2, self.csop2, self.sop2), (self.cond3, self.csop3, self.sop3), (self.cond4, self.csop4, self.sop4), (self.cond5, self.csop5, self.sop5), (self.cond6, self.csop6, self.sop6), (self.cond7, self.csop7, self.sop7), (self.cond8, self.csop8, self.sop8)]
        self.axiom = AxiomEmpty()

    def cond0(self, state, argv):
        newPersonId = argv['Op_Admin_createNewUser_run_8426']['newPersonId']
        firstName = argv['Op_Admin_createNewUser_run_8426']['firstName']
        lastName = argv['Op_Admin_createNewUser_run_8426']['lastName']
        nic = argv['Op_Admin_createNewUser_run_8426']['nic']
        mobile = argv['Op_Admin_createNewUser_run_8426']['mobile']
        newUserId = argv['Op_Admin_createNewUser_run_8426']['newUserId']
        userName = argv['Op_Admin_createNewUser_run_8426']['userName']
        userType = argv['Op_Admin_createNewUser_run_8426']['userType']
        newLabAssistantId = argv['Op_Admin_createNewUser_run_8426']['newLabAssistantId']
        newPersonId = argv['Op_Admin_createNewUser_run_8426']['newPersonId']
        firstName = argv['Op_Admin_createNewUser_run_8426']['firstName']
        lastName = argv['Op_Admin_createNewUser_run_8426']['lastName']
        nic = argv['Op_Admin_createNewUser_run_8426']['nic']
        mobile = argv['Op_Admin_createNewUser_run_8426']['mobile']
        newUserId = argv['Op_Admin_createNewUser_run_8426']['newUserId']
        userName = argv['Op_Admin_createNewUser_run_8426']['userName']
        userType = argv['Op_Admin_createNewUser_run_8426']['userType']
        newLabAssistantId = argv['Op_Admin_createNewUser_run_8426']['newLabAssistantId']
        newPersonId = argv['Op_Admin_createNewUser_run_8426']['newPersonId']
        firstName = argv['Op_Admin_createNewUser_run_8426']['firstName']
        lastName = argv['Op_Admin_createNewUser_run_8426']['lastName']
        nic = argv['Op_Admin_createNewUser_run_8426']['nic']
        mobile = argv['Op_Admin_createNewUser_run_8426']['mobile']
        newUserId = argv['Op_Admin_createNewUser_run_8426']['newUserId']
        userName = argv['Op_Admin_createNewUser_run_8426']['userName']
        userType = argv['Op_Admin_createNewUser_run_8426']['userType']
        newPharmacistId = argv['Op_Admin_createNewUser_run_8426']['newPharmacistId']
        newPersonId = argv['Op_Admin_createNewUser_run_8426']['newPersonId']
        firstName = argv['Op_Admin_createNewUser_run_8426']['firstName']
        lastName = argv['Op_Admin_createNewUser_run_8426']['lastName']
        nic = argv['Op_Admin_createNewUser_run_8426']['nic']
        mobile = argv['Op_Admin_createNewUser_run_8426']['mobile']
        newUserId = argv['Op_Admin_createNewUser_run_8426']['newUserId']
        userName = argv['Op_Admin_createNewUser_run_8426']['userName']
        userType = argv['Op_Admin_createNewUser_run_8426']['userType']
        newSlmcReg = argv['Op_Admin_createNewUser_run_8426']['newSlmcReg']
        newPersonId = argv['Op_Admin_createNewUser_run_8426']['newPersonId']
        firstName = argv['Op_Admin_createNewUser_run_8426']['firstName']
        lastName = argv['Op_Admin_createNewUser_run_8426']['lastName']
        nic = argv['Op_Admin_createNewUser_run_8426']['nic']
        mobile = argv['Op_Admin_createNewUser_run_8426']['mobile']
        newUserId = argv['Op_Admin_createNewUser_run_8426']['newUserId']
        userName = argv['Op_Admin_createNewUser_run_8426']['userName']
        userType = argv['Op_Admin_createNewUser_run_8426']['userType']
        newLabAssistantId = argv['Op_Admin_createNewUser_run_8426']['newLabAssistantId']
        newPersonId = argv['Op_Admin_createNewUser_run_8426']['newPersonId']
        firstName = argv['Op_Admin_createNewUser_run_8426']['firstName']
        lastName = argv['Op_Admin_createNewUser_run_8426']['lastName']
        nic = argv['Op_Admin_createNewUser_run_8426']['nic']
        mobile = argv['Op_Admin_createNewUser_run_8426']['mobile']
        newUserId = argv['Op_Admin_createNewUser_run_8426']['newUserId']
        userName = argv['Op_Admin_createNewUser_run_8426']['userName']
        userType = argv['Op_Admin_createNewUser_run_8426']['userType']
        newPharmacistId = argv['Op_Admin_createNewUser_run_8426']['newPharmacistId']
        newPersonId = argv['Op_Admin_createNewUser_run_8426']['newPersonId']
        firstName = argv['Op_Admin_createNewUser_run_8426']['firstName']
        lastName = argv['Op_Admin_createNewUser_run_8426']['lastName']
        nic = argv['Op_Admin_createNewUser_run_8426']['nic']
        mobile = argv['Op_Admin_createNewUser_run_8426']['mobile']
        newUserId = argv['Op_Admin_createNewUser_run_8426']['newUserId']
        userName = argv['Op_Admin_createNewUser_run_8426']['userName']
        userType = argv['Op_Admin_createNewUser_run_8426']['userType']
        newSlmcReg = argv['Op_Admin_createNewUser_run_8426']['newSlmcReg']
        return And((argv['Op_Admin_createNewUser_run_8426']['userType'])==(StringVal('doctor')),(argv['Op_Admin_createNewUser_run_8426']['userType'])==(StringVal('lab_assistant')),Not((argv['Op_Admin_createNewUser_run_8426']['userType'])==(StringVal('doctor'))),Not((argv['Op_Admin_createNewUser_run_8426']['userType'])==(StringVal('lab_assistant'))),Not((argv['Op_Admin_createNewUser_run_8426']['userType'])==(StringVal('doctor'))),Not((argv['Op_Admin_createNewUser_run_8426']['userType'])==(StringVal('lab_assistant'))),Not((argv['Op_Admin_createNewUser_run_8426']['userType'])==(StringVal('pharmacist'))),Not((argv['Op_Admin_createNewUser_run_8426']['userType'])==(StringVal('doctor'))),Not((argv['Op_Admin_createNewUser_run_8426']['userType'])==(StringVal('doctor'))),Not((argv['Op_Admin_createNewUser_run_8426']['userType'])==(StringVal('lab_assistant'))),Not((argv['Op_Admin_createNewUser_run_8426']['userType'])==(StringVal('doctor'))),Not((argv['Op_Admin_createNewUser_run_8426']['userType'])==(StringVal('lab_assistant'))),Not((argv['Op_Admin_createNewUser_run_8426']['userType'])==(StringVal('pharmacist'))),Not((argv['Op_Admin_createNewUser_run_8426']['userType'])==(StringVal('doctor'))))

    def csop0(self, state, argv):
        return True

    def sop0(self, state, argv):
        newPersonId = argv['Op_Admin_createNewUser_run_8426']['newPersonId']
        firstName = argv['Op_Admin_createNewUser_run_8426']['firstName']
        lastName = argv['Op_Admin_createNewUser_run_8426']['lastName']
        nic = argv['Op_Admin_createNewUser_run_8426']['nic']
        mobile = argv['Op_Admin_createNewUser_run_8426']['mobile']
        newUserId = argv['Op_Admin_createNewUser_run_8426']['newUserId']
        userName = argv['Op_Admin_createNewUser_run_8426']['userName']
        userType = argv['Op_Admin_createNewUser_run_8426']['userType']
        newLabAssistantId = argv['Op_Admin_createNewUser_run_8426']['newLabAssistantId']
        person_person_id = argv['Op_Admin_createNewUser_run_8426']['newPersonId']
        person_first_name = argv['Op_Admin_createNewUser_run_8426']['firstName']
        person_last_name = argv['Op_Admin_createNewUser_run_8426']['lastName']
        person_nic = argv['Op_Admin_createNewUser_run_8426']['nic']
        person_mobile = argv['Op_Admin_createNewUser_run_8426']['mobile']
        state['TABLE_person'].add({'person_id': person_person_id}, {'first_name': person_first_name,'last_name': person_last_name,'nic': person_nic,'mobile': person_mobile})
        return state

    def cond1(self, state, argv):
        newPersonId = argv['Op_Admin_createNewUser_run_8426']['newPersonId']
        firstName = argv['Op_Admin_createNewUser_run_8426']['firstName']
        lastName = argv['Op_Admin_createNewUser_run_8426']['lastName']
        nic = argv['Op_Admin_createNewUser_run_8426']['nic']
        mobile = argv['Op_Admin_createNewUser_run_8426']['mobile']
        newUserId = argv['Op_Admin_createNewUser_run_8426']['newUserId']
        userName = argv['Op_Admin_createNewUser_run_8426']['userName']
        userType = argv['Op_Admin_createNewUser_run_8426']['userType']
        newPharmacistId = argv['Op_Admin_createNewUser_run_8426']['newPharmacistId']
        newPersonId = argv['Op_Admin_createNewUser_run_8426']['newPersonId']
        firstName = argv['Op_Admin_createNewUser_run_8426']['firstName']
        lastName = argv['Op_Admin_createNewUser_run_8426']['lastName']
        nic = argv['Op_Admin_createNewUser_run_8426']['nic']
        mobile = argv['Op_Admin_createNewUser_run_8426']['mobile']
        newUserId = argv['Op_Admin_createNewUser_run_8426']['newUserId']
        userName = argv['Op_Admin_createNewUser_run_8426']['userName']
        userType = argv['Op_Admin_createNewUser_run_8426']['userType']
        newLabAssistantId = argv['Op_Admin_createNewUser_run_8426']['newLabAssistantId']
        newPersonId = argv['Op_Admin_createNewUser_run_8426']['newPersonId']
        firstName = argv['Op_Admin_createNewUser_run_8426']['firstName']
        lastName = argv['Op_Admin_createNewUser_run_8426']['lastName']
        nic = argv['Op_Admin_createNewUser_run_8426']['nic']
        mobile = argv['Op_Admin_createNewUser_run_8426']['mobile']
        newUserId = argv['Op_Admin_createNewUser_run_8426']['newUserId']
        userName = argv['Op_Admin_createNewUser_run_8426']['userName']
        userType = argv['Op_Admin_createNewUser_run_8426']['userType']
        newPharmacistId = argv['Op_Admin_createNewUser_run_8426']['newPharmacistId']
        newPersonId = argv['Op_Admin_createNewUser_run_8426']['newPersonId']
        firstName = argv['Op_Admin_createNewUser_run_8426']['firstName']
        lastName = argv['Op_Admin_createNewUser_run_8426']['lastName']
        nic = argv['Op_Admin_createNewUser_run_8426']['nic']
        mobile = argv['Op_Admin_createNewUser_run_8426']['mobile']
        newUserId = argv['Op_Admin_createNewUser_run_8426']['newUserId']
        userName = argv['Op_Admin_createNewUser_run_8426']['userName']
        userType = argv['Op_Admin_createNewUser_run_8426']['userType']
        newSlmcReg = argv['Op_Admin_createNewUser_run_8426']['newSlmcReg']
        newPersonId = argv['Op_Admin_createNewUser_run_8426']['newPersonId']
        firstName = argv['Op_Admin_createNewUser_run_8426']['firstName']
        lastName = argv['Op_Admin_createNewUser_run_8426']['lastName']
        nic = argv['Op_Admin_createNewUser_run_8426']['nic']
        mobile = argv['Op_Admin_createNewUser_run_8426']['mobile']
        newUserId = argv['Op_Admin_createNewUser_run_8426']['newUserId']
        userName = argv['Op_Admin_createNewUser_run_8426']['userName']
        userType = argv['Op_Admin_createNewUser_run_8426']['userType']
        newLabAssistantId = argv['Op_Admin_createNewUser_run_8426']['newLabAssistantId']
        newPersonId = argv['Op_Admin_createNewUser_run_8426']['newPersonId']
        firstName = argv['Op_Admin_createNewUser_run_8426']['firstName']
        lastName = argv['Op_Admin_createNewUser_run_8426']['lastName']
        nic = argv['Op_Admin_createNewUser_run_8426']['nic']
        mobile = argv['Op_Admin_createNewUser_run_8426']['mobile']
        newUserId = argv['Op_Admin_createNewUser_run_8426']['newUserId']
        userName = argv['Op_Admin_createNewUser_run_8426']['userName']
        userType = argv['Op_Admin_createNewUser_run_8426']['userType']
        newPharmacistId = argv['Op_Admin_createNewUser_run_8426']['newPharmacistId']
        newPersonId = argv['Op_Admin_createNewUser_run_8426']['newPersonId']
        firstName = argv['Op_Admin_createNewUser_run_8426']['firstName']
        lastName = argv['Op_Admin_createNewUser_run_8426']['lastName']
        nic = argv['Op_Admin_createNewUser_run_8426']['nic']
        mobile = argv['Op_Admin_createNewUser_run_8426']['mobile']
        newUserId = argv['Op_Admin_createNewUser_run_8426']['newUserId']
        userName = argv['Op_Admin_createNewUser_run_8426']['userName']
        userType = argv['Op_Admin_createNewUser_run_8426']['userType']
        newSlmcReg = argv['Op_Admin_createNewUser_run_8426']['newSlmcReg']
        return And((argv['Op_Admin_createNewUser_run_8426']['userType'])==(StringVal('doctor')),(argv['Op_Admin_createNewUser_run_8426']['userType'])==(StringVal('lab_assistant')),(argv['Op_Admin_createNewUser_run_8426']['userType'])==(StringVal('pharmacist')),Not((argv['Op_Admin_createNewUser_run_8426']['userType'])==(StringVal('doctor'))),Not((argv['Op_Admin_createNewUser_run_8426']['userType'])==(StringVal('lab_assistant'))),Not((argv['Op_Admin_createNewUser_run_8426']['userType'])==(StringVal('doctor'))),Not((argv['Op_Admin_createNewUser_run_8426']['userType'])==(StringVal('lab_assistant'))),Not((argv['Op_Admin_createNewUser_run_8426']['userType'])==(StringVal('pharmacist'))),Not((argv['Op_Admin_createNewUser_run_8426']['userType'])==(StringVal('doctor'))),Not((argv['Op_Admin_createNewUser_run_8426']['userType'])==(StringVal('doctor'))),Not((argv['Op_Admin_createNewUser_run_8426']['userType'])==(StringVal('lab_assistant'))),Not((argv['Op_Admin_createNewUser_run_8426']['userType'])==(StringVal('doctor'))),Not((argv['Op_Admin_createNewUser_run_8426']['userType'])==(StringVal('lab_assistant'))),Not((argv['Op_Admin_createNewUser_run_8426']['userType'])==(StringVal('pharmacist'))),Not((argv['Op_Admin_createNewUser_run_8426']['userType'])==(StringVal('doctor'))))

    def csop1(self, state, argv):
        return True

    def sop1(self, state, argv):
        newPersonId = argv['Op_Admin_createNewUser_run_8426']['newPersonId']
        firstName = argv['Op_Admin_createNewUser_run_8426']['firstName']
        lastName = argv['Op_Admin_createNewUser_run_8426']['lastName']
        nic = argv['Op_Admin_createNewUser_run_8426']['nic']
        mobile = argv['Op_Admin_createNewUser_run_8426']['mobile']
        newUserId = argv['Op_Admin_createNewUser_run_8426']['newUserId']
        userName = argv['Op_Admin_createNewUser_run_8426']['userName']
        userType = argv['Op_Admin_createNewUser_run_8426']['userType']
        newPharmacistId = argv['Op_Admin_createNewUser_run_8426']['newPharmacistId']
        person_person_id = argv['Op_Admin_createNewUser_run_8426']['newPersonId']
        person_first_name = argv['Op_Admin_createNewUser_run_8426']['firstName']
        person_last_name = argv['Op_Admin_createNewUser_run_8426']['lastName']
        person_nic = argv['Op_Admin_createNewUser_run_8426']['nic']
        person_mobile = argv['Op_Admin_createNewUser_run_8426']['mobile']
        state['TABLE_person'].add({'person_id': person_person_id}, {'first_name': person_first_name,'last_name': person_last_name,'nic': person_nic,'mobile': person_mobile})
        return state

    def cond2(self, state, argv):
        newPersonId = argv['Op_Admin_createNewUser_run_8426']['newPersonId']
        firstName = argv['Op_Admin_createNewUser_run_8426']['firstName']
        lastName = argv['Op_Admin_createNewUser_run_8426']['lastName']
        nic = argv['Op_Admin_createNewUser_run_8426']['nic']
        mobile = argv['Op_Admin_createNewUser_run_8426']['mobile']
        newUserId = argv['Op_Admin_createNewUser_run_8426']['newUserId']
        userName = argv['Op_Admin_createNewUser_run_8426']['userName']
        userType = argv['Op_Admin_createNewUser_run_8426']['userType']
        newSlmcReg = argv['Op_Admin_createNewUser_run_8426']['newSlmcReg']
        newPersonId = argv['Op_Admin_createNewUser_run_8426']['newPersonId']
        firstName = argv['Op_Admin_createNewUser_run_8426']['firstName']
        lastName = argv['Op_Admin_createNewUser_run_8426']['lastName']
        nic = argv['Op_Admin_createNewUser_run_8426']['nic']
        mobile = argv['Op_Admin_createNewUser_run_8426']['mobile']
        newUserId = argv['Op_Admin_createNewUser_run_8426']['newUserId']
        userName = argv['Op_Admin_createNewUser_run_8426']['userName']
        userType = argv['Op_Admin_createNewUser_run_8426']['userType']
        newLabAssistantId = argv['Op_Admin_createNewUser_run_8426']['newLabAssistantId']
        newPersonId = argv['Op_Admin_createNewUser_run_8426']['newPersonId']
        firstName = argv['Op_Admin_createNewUser_run_8426']['firstName']
        lastName = argv['Op_Admin_createNewUser_run_8426']['lastName']
        nic = argv['Op_Admin_createNewUser_run_8426']['nic']
        mobile = argv['Op_Admin_createNewUser_run_8426']['mobile']
        newUserId = argv['Op_Admin_createNewUser_run_8426']['newUserId']
        userName = argv['Op_Admin_createNewUser_run_8426']['userName']
        userType = argv['Op_Admin_createNewUser_run_8426']['userType']
        newPharmacistId = argv['Op_Admin_createNewUser_run_8426']['newPharmacistId']
        newPersonId = argv['Op_Admin_createNewUser_run_8426']['newPersonId']
        firstName = argv['Op_Admin_createNewUser_run_8426']['firstName']
        lastName = argv['Op_Admin_createNewUser_run_8426']['lastName']
        nic = argv['Op_Admin_createNewUser_run_8426']['nic']
        mobile = argv['Op_Admin_createNewUser_run_8426']['mobile']
        newUserId = argv['Op_Admin_createNewUser_run_8426']['newUserId']
        userName = argv['Op_Admin_createNewUser_run_8426']['userName']
        userType = argv['Op_Admin_createNewUser_run_8426']['userType']
        newSlmcReg = argv['Op_Admin_createNewUser_run_8426']['newSlmcReg']
        newPersonId = argv['Op_Admin_createNewUser_run_8426']['newPersonId']
        firstName = argv['Op_Admin_createNewUser_run_8426']['firstName']
        lastName = argv['Op_Admin_createNewUser_run_8426']['lastName']
        nic = argv['Op_Admin_createNewUser_run_8426']['nic']
        mobile = argv['Op_Admin_createNewUser_run_8426']['mobile']
        newUserId = argv['Op_Admin_createNewUser_run_8426']['newUserId']
        userName = argv['Op_Admin_createNewUser_run_8426']['userName']
        userType = argv['Op_Admin_createNewUser_run_8426']['userType']
        newLabAssistantId = argv['Op_Admin_createNewUser_run_8426']['newLabAssistantId']
        newPersonId = argv['Op_Admin_createNewUser_run_8426']['newPersonId']
        firstName = argv['Op_Admin_createNewUser_run_8426']['firstName']
        lastName = argv['Op_Admin_createNewUser_run_8426']['lastName']
        nic = argv['Op_Admin_createNewUser_run_8426']['nic']
        mobile = argv['Op_Admin_createNewUser_run_8426']['mobile']
        newUserId = argv['Op_Admin_createNewUser_run_8426']['newUserId']
        userName = argv['Op_Admin_createNewUser_run_8426']['userName']
        userType = argv['Op_Admin_createNewUser_run_8426']['userType']
        newPharmacistId = argv['Op_Admin_createNewUser_run_8426']['newPharmacistId']
        newPersonId = argv['Op_Admin_createNewUser_run_8426']['newPersonId']
        firstName = argv['Op_Admin_createNewUser_run_8426']['firstName']
        lastName = argv['Op_Admin_createNewUser_run_8426']['lastName']
        nic = argv['Op_Admin_createNewUser_run_8426']['nic']
        mobile = argv['Op_Admin_createNewUser_run_8426']['mobile']
        newUserId = argv['Op_Admin_createNewUser_run_8426']['newUserId']
        userName = argv['Op_Admin_createNewUser_run_8426']['userName']
        userType = argv['Op_Admin_createNewUser_run_8426']['userType']
        newSlmcReg = argv['Op_Admin_createNewUser_run_8426']['newSlmcReg']
        return And((argv['Op_Admin_createNewUser_run_8426']['userType'])==(StringVal('doctor')),Not((argv['Op_Admin_createNewUser_run_8426']['userType'])==(StringVal('doctor'))),Not((argv['Op_Admin_createNewUser_run_8426']['userType'])==(StringVal('lab_assistant'))),Not((argv['Op_Admin_createNewUser_run_8426']['userType'])==(StringVal('doctor'))),Not((argv['Op_Admin_createNewUser_run_8426']['userType'])==(StringVal('lab_assistant'))),Not((argv['Op_Admin_createNewUser_run_8426']['userType'])==(StringVal('pharmacist'))),Not((argv['Op_Admin_createNewUser_run_8426']['userType'])==(StringVal('doctor'))),Not((argv['Op_Admin_createNewUser_run_8426']['userType'])==(StringVal('doctor'))),Not((argv['Op_Admin_createNewUser_run_8426']['userType'])==(StringVal('lab_assistant'))),Not((argv['Op_Admin_createNewUser_run_8426']['userType'])==(StringVal('doctor'))),Not((argv['Op_Admin_createNewUser_run_8426']['userType'])==(StringVal('lab_assistant'))),Not((argv['Op_Admin_createNewUser_run_8426']['userType'])==(StringVal('pharmacist'))),Not((argv['Op_Admin_createNewUser_run_8426']['userType'])==(StringVal('doctor'))))

    def csop2(self, state, argv):
        return True

    def sop2(self, state, argv):
        newPersonId = argv['Op_Admin_createNewUser_run_8426']['newPersonId']
        firstName = argv['Op_Admin_createNewUser_run_8426']['firstName']
        lastName = argv['Op_Admin_createNewUser_run_8426']['lastName']
        nic = argv['Op_Admin_createNewUser_run_8426']['nic']
        mobile = argv['Op_Admin_createNewUser_run_8426']['mobile']
        newUserId = argv['Op_Admin_createNewUser_run_8426']['newUserId']
        userName = argv['Op_Admin_createNewUser_run_8426']['userName']
        userType = argv['Op_Admin_createNewUser_run_8426']['userType']
        newSlmcReg = argv['Op_Admin_createNewUser_run_8426']['newSlmcReg']
        person_person_id = argv['Op_Admin_createNewUser_run_8426']['newPersonId']
        person_first_name = argv['Op_Admin_createNewUser_run_8426']['firstName']
        person_last_name = argv['Op_Admin_createNewUser_run_8426']['lastName']
        person_nic = argv['Op_Admin_createNewUser_run_8426']['nic']
        person_mobile = argv['Op_Admin_createNewUser_run_8426']['mobile']
        state['TABLE_person'].add({'person_id': person_person_id}, {'first_name': person_first_name,'last_name': person_last_name,'nic': person_nic,'mobile': person_mobile})
        return state

    def cond3(self, state, argv):
        newPersonId = argv['Op_Admin_createNewUser_run_8426']['newPersonId']
        firstName = argv['Op_Admin_createNewUser_run_8426']['firstName']
        lastName = argv['Op_Admin_createNewUser_run_8426']['lastName']
        nic = argv['Op_Admin_createNewUser_run_8426']['nic']
        mobile = argv['Op_Admin_createNewUser_run_8426']['mobile']
        newUserId = argv['Op_Admin_createNewUser_run_8426']['newUserId']
        userName = argv['Op_Admin_createNewUser_run_8426']['userName']
        userType = argv['Op_Admin_createNewUser_run_8426']['userType']
        newLabAssistantId = argv['Op_Admin_createNewUser_run_8426']['newLabAssistantId']
        newPersonId = argv['Op_Admin_createNewUser_run_8426']['newPersonId']
        firstName = argv['Op_Admin_createNewUser_run_8426']['firstName']
        lastName = argv['Op_Admin_createNewUser_run_8426']['lastName']
        nic = argv['Op_Admin_createNewUser_run_8426']['nic']
        mobile = argv['Op_Admin_createNewUser_run_8426']['mobile']
        newUserId = argv['Op_Admin_createNewUser_run_8426']['newUserId']
        userName = argv['Op_Admin_createNewUser_run_8426']['userName']
        userType = argv['Op_Admin_createNewUser_run_8426']['userType']
        newLabAssistantId = argv['Op_Admin_createNewUser_run_8426']['newLabAssistantId']
        newPersonId = argv['Op_Admin_createNewUser_run_8426']['newPersonId']
        firstName = argv['Op_Admin_createNewUser_run_8426']['firstName']
        lastName = argv['Op_Admin_createNewUser_run_8426']['lastName']
        nic = argv['Op_Admin_createNewUser_run_8426']['nic']
        mobile = argv['Op_Admin_createNewUser_run_8426']['mobile']
        newUserId = argv['Op_Admin_createNewUser_run_8426']['newUserId']
        userName = argv['Op_Admin_createNewUser_run_8426']['userName']
        userType = argv['Op_Admin_createNewUser_run_8426']['userType']
        newPharmacistId = argv['Op_Admin_createNewUser_run_8426']['newPharmacistId']
        newPersonId = argv['Op_Admin_createNewUser_run_8426']['newPersonId']
        firstName = argv['Op_Admin_createNewUser_run_8426']['firstName']
        lastName = argv['Op_Admin_createNewUser_run_8426']['lastName']
        nic = argv['Op_Admin_createNewUser_run_8426']['nic']
        mobile = argv['Op_Admin_createNewUser_run_8426']['mobile']
        newUserId = argv['Op_Admin_createNewUser_run_8426']['newUserId']
        userName = argv['Op_Admin_createNewUser_run_8426']['userName']
        userType = argv['Op_Admin_createNewUser_run_8426']['userType']
        newSlmcReg = argv['Op_Admin_createNewUser_run_8426']['newSlmcReg']
        return And((argv['Op_Admin_createNewUser_run_8426']['userType'])==(StringVal('doctor')),(argv['Op_Admin_createNewUser_run_8426']['userType'])==(StringVal('lab_assistant')),Not((argv['Op_Admin_createNewUser_run_8426']['userType'])==(StringVal('doctor'))),Not((argv['Op_Admin_createNewUser_run_8426']['userType'])==(StringVal('lab_assistant'))),Not((argv['Op_Admin_createNewUser_run_8426']['userType'])==(StringVal('doctor'))),Not((argv['Op_Admin_createNewUser_run_8426']['userType'])==(StringVal('lab_assistant'))),Not((argv['Op_Admin_createNewUser_run_8426']['userType'])==(StringVal('pharmacist'))),Not((argv['Op_Admin_createNewUser_run_8426']['userType'])==(StringVal('doctor'))))

    def csop3(self, state, argv):
        return True

    def sop3(self, state, argv):
        newPersonId = argv['Op_Admin_createNewUser_run_8426']['newPersonId']
        firstName = argv['Op_Admin_createNewUser_run_8426']['firstName']
        lastName = argv['Op_Admin_createNewUser_run_8426']['lastName']
        nic = argv['Op_Admin_createNewUser_run_8426']['nic']
        mobile = argv['Op_Admin_createNewUser_run_8426']['mobile']
        newUserId = argv['Op_Admin_createNewUser_run_8426']['newUserId']
        userName = argv['Op_Admin_createNewUser_run_8426']['userName']
        userType = argv['Op_Admin_createNewUser_run_8426']['userType']
        newLabAssistantId = argv['Op_Admin_createNewUser_run_8426']['newLabAssistantId']
        person_person_id = argv['Op_Admin_createNewUser_run_8426']['newPersonId']
        person_first_name = argv['Op_Admin_createNewUser_run_8426']['firstName']
        person_last_name = argv['Op_Admin_createNewUser_run_8426']['lastName']
        person_nic = argv['Op_Admin_createNewUser_run_8426']['nic']
        person_mobile = argv['Op_Admin_createNewUser_run_8426']['mobile']
        state['TABLE_person'].add({'person_id': person_person_id}, {'first_name': person_first_name,'last_name': person_last_name,'nic': person_nic,'mobile': person_mobile})
        sys_user_person_id = argv['Op_Admin_createNewUser_run_8426']['newPersonId']
        sys_user_user_id = argv['Op_Admin_createNewUser_run_8426']['newUserId']
        sys_user_user_name = argv['Op_Admin_createNewUser_run_8426']['userName']
        sys_user_user_type = argv['Op_Admin_createNewUser_run_8426']['userType']
        sys_user_password = StringVal('1234')
        state['TABLE_sys_user'].add({'user_id': sys_user_user_id}, {'person_id': sys_user_person_id,'user_name': sys_user_user_name,'user_type': sys_user_user_type,'password': sys_user_password})
        return state

    def cond4(self, state, argv):
        newPersonId = argv['Op_Admin_createNewUser_run_8426']['newPersonId']
        firstName = argv['Op_Admin_createNewUser_run_8426']['firstName']
        lastName = argv['Op_Admin_createNewUser_run_8426']['lastName']
        nic = argv['Op_Admin_createNewUser_run_8426']['nic']
        mobile = argv['Op_Admin_createNewUser_run_8426']['mobile']
        newUserId = argv['Op_Admin_createNewUser_run_8426']['newUserId']
        userName = argv['Op_Admin_createNewUser_run_8426']['userName']
        userType = argv['Op_Admin_createNewUser_run_8426']['userType']
        newPharmacistId = argv['Op_Admin_createNewUser_run_8426']['newPharmacistId']
        newPersonId = argv['Op_Admin_createNewUser_run_8426']['newPersonId']
        firstName = argv['Op_Admin_createNewUser_run_8426']['firstName']
        lastName = argv['Op_Admin_createNewUser_run_8426']['lastName']
        nic = argv['Op_Admin_createNewUser_run_8426']['nic']
        mobile = argv['Op_Admin_createNewUser_run_8426']['mobile']
        newUserId = argv['Op_Admin_createNewUser_run_8426']['newUserId']
        userName = argv['Op_Admin_createNewUser_run_8426']['userName']
        userType = argv['Op_Admin_createNewUser_run_8426']['userType']
        newLabAssistantId = argv['Op_Admin_createNewUser_run_8426']['newLabAssistantId']
        newPersonId = argv['Op_Admin_createNewUser_run_8426']['newPersonId']
        firstName = argv['Op_Admin_createNewUser_run_8426']['firstName']
        lastName = argv['Op_Admin_createNewUser_run_8426']['lastName']
        nic = argv['Op_Admin_createNewUser_run_8426']['nic']
        mobile = argv['Op_Admin_createNewUser_run_8426']['mobile']
        newUserId = argv['Op_Admin_createNewUser_run_8426']['newUserId']
        userName = argv['Op_Admin_createNewUser_run_8426']['userName']
        userType = argv['Op_Admin_createNewUser_run_8426']['userType']
        newPharmacistId = argv['Op_Admin_createNewUser_run_8426']['newPharmacistId']
        newPersonId = argv['Op_Admin_createNewUser_run_8426']['newPersonId']
        firstName = argv['Op_Admin_createNewUser_run_8426']['firstName']
        lastName = argv['Op_Admin_createNewUser_run_8426']['lastName']
        nic = argv['Op_Admin_createNewUser_run_8426']['nic']
        mobile = argv['Op_Admin_createNewUser_run_8426']['mobile']
        newUserId = argv['Op_Admin_createNewUser_run_8426']['newUserId']
        userName = argv['Op_Admin_createNewUser_run_8426']['userName']
        userType = argv['Op_Admin_createNewUser_run_8426']['userType']
        newSlmcReg = argv['Op_Admin_createNewUser_run_8426']['newSlmcReg']
        return And((argv['Op_Admin_createNewUser_run_8426']['userType'])==(StringVal('doctor')),(argv['Op_Admin_createNewUser_run_8426']['userType'])==(StringVal('lab_assistant')),(argv['Op_Admin_createNewUser_run_8426']['userType'])==(StringVal('pharmacist')),Not((argv['Op_Admin_createNewUser_run_8426']['userType'])==(StringVal('doctor'))),Not((argv['Op_Admin_createNewUser_run_8426']['userType'])==(StringVal('lab_assistant'))),Not((argv['Op_Admin_createNewUser_run_8426']['userType'])==(StringVal('doctor'))),Not((argv['Op_Admin_createNewUser_run_8426']['userType'])==(StringVal('lab_assistant'))),Not((argv['Op_Admin_createNewUser_run_8426']['userType'])==(StringVal('pharmacist'))),Not((argv['Op_Admin_createNewUser_run_8426']['userType'])==(StringVal('doctor'))))

    def csop4(self, state, argv):
        return True

    def sop4(self, state, argv):
        newPersonId = argv['Op_Admin_createNewUser_run_8426']['newPersonId']
        firstName = argv['Op_Admin_createNewUser_run_8426']['firstName']
        lastName = argv['Op_Admin_createNewUser_run_8426']['lastName']
        nic = argv['Op_Admin_createNewUser_run_8426']['nic']
        mobile = argv['Op_Admin_createNewUser_run_8426']['mobile']
        newUserId = argv['Op_Admin_createNewUser_run_8426']['newUserId']
        userName = argv['Op_Admin_createNewUser_run_8426']['userName']
        userType = argv['Op_Admin_createNewUser_run_8426']['userType']
        newPharmacistId = argv['Op_Admin_createNewUser_run_8426']['newPharmacistId']
        person_person_id = argv['Op_Admin_createNewUser_run_8426']['newPersonId']
        person_first_name = argv['Op_Admin_createNewUser_run_8426']['firstName']
        person_last_name = argv['Op_Admin_createNewUser_run_8426']['lastName']
        person_nic = argv['Op_Admin_createNewUser_run_8426']['nic']
        person_mobile = argv['Op_Admin_createNewUser_run_8426']['mobile']
        state['TABLE_person'].add({'person_id': person_person_id}, {'first_name': person_first_name,'last_name': person_last_name,'nic': person_nic,'mobile': person_mobile})
        sys_user_person_id = argv['Op_Admin_createNewUser_run_8426']['newPersonId']
        sys_user_user_id = argv['Op_Admin_createNewUser_run_8426']['newUserId']
        sys_user_user_name = argv['Op_Admin_createNewUser_run_8426']['userName']
        sys_user_user_type = argv['Op_Admin_createNewUser_run_8426']['userType']
        sys_user_password = StringVal('1234')
        state['TABLE_sys_user'].add({'user_id': sys_user_user_id}, {'person_id': sys_user_person_id,'user_name': sys_user_user_name,'user_type': sys_user_user_type,'password': sys_user_password})
        return state

    def cond5(self, state, argv):
        newPersonId = argv['Op_Admin_createNewUser_run_8426']['newPersonId']
        firstName = argv['Op_Admin_createNewUser_run_8426']['firstName']
        lastName = argv['Op_Admin_createNewUser_run_8426']['lastName']
        nic = argv['Op_Admin_createNewUser_run_8426']['nic']
        mobile = argv['Op_Admin_createNewUser_run_8426']['mobile']
        newUserId = argv['Op_Admin_createNewUser_run_8426']['newUserId']
        userName = argv['Op_Admin_createNewUser_run_8426']['userName']
        userType = argv['Op_Admin_createNewUser_run_8426']['userType']
        newSlmcReg = argv['Op_Admin_createNewUser_run_8426']['newSlmcReg']
        newPersonId = argv['Op_Admin_createNewUser_run_8426']['newPersonId']
        firstName = argv['Op_Admin_createNewUser_run_8426']['firstName']
        lastName = argv['Op_Admin_createNewUser_run_8426']['lastName']
        nic = argv['Op_Admin_createNewUser_run_8426']['nic']
        mobile = argv['Op_Admin_createNewUser_run_8426']['mobile']
        newUserId = argv['Op_Admin_createNewUser_run_8426']['newUserId']
        userName = argv['Op_Admin_createNewUser_run_8426']['userName']
        userType = argv['Op_Admin_createNewUser_run_8426']['userType']
        newLabAssistantId = argv['Op_Admin_createNewUser_run_8426']['newLabAssistantId']
        newPersonId = argv['Op_Admin_createNewUser_run_8426']['newPersonId']
        firstName = argv['Op_Admin_createNewUser_run_8426']['firstName']
        lastName = argv['Op_Admin_createNewUser_run_8426']['lastName']
        nic = argv['Op_Admin_createNewUser_run_8426']['nic']
        mobile = argv['Op_Admin_createNewUser_run_8426']['mobile']
        newUserId = argv['Op_Admin_createNewUser_run_8426']['newUserId']
        userName = argv['Op_Admin_createNewUser_run_8426']['userName']
        userType = argv['Op_Admin_createNewUser_run_8426']['userType']
        newPharmacistId = argv['Op_Admin_createNewUser_run_8426']['newPharmacistId']
        newPersonId = argv['Op_Admin_createNewUser_run_8426']['newPersonId']
        firstName = argv['Op_Admin_createNewUser_run_8426']['firstName']
        lastName = argv['Op_Admin_createNewUser_run_8426']['lastName']
        nic = argv['Op_Admin_createNewUser_run_8426']['nic']
        mobile = argv['Op_Admin_createNewUser_run_8426']['mobile']
        newUserId = argv['Op_Admin_createNewUser_run_8426']['newUserId']
        userName = argv['Op_Admin_createNewUser_run_8426']['userName']
        userType = argv['Op_Admin_createNewUser_run_8426']['userType']
        newSlmcReg = argv['Op_Admin_createNewUser_run_8426']['newSlmcReg']
        return And((argv['Op_Admin_createNewUser_run_8426']['userType'])==(StringVal('doctor')),Not((argv['Op_Admin_createNewUser_run_8426']['userType'])==(StringVal('doctor'))),Not((argv['Op_Admin_createNewUser_run_8426']['userType'])==(StringVal('lab_assistant'))),Not((argv['Op_Admin_createNewUser_run_8426']['userType'])==(StringVal('doctor'))),Not((argv['Op_Admin_createNewUser_run_8426']['userType'])==(StringVal('lab_assistant'))),Not((argv['Op_Admin_createNewUser_run_8426']['userType'])==(StringVal('pharmacist'))),Not((argv['Op_Admin_createNewUser_run_8426']['userType'])==(StringVal('doctor'))))

    def csop5(self, state, argv):
        return True

    def sop5(self, state, argv):
        newPersonId = argv['Op_Admin_createNewUser_run_8426']['newPersonId']
        firstName = argv['Op_Admin_createNewUser_run_8426']['firstName']
        lastName = argv['Op_Admin_createNewUser_run_8426']['lastName']
        nic = argv['Op_Admin_createNewUser_run_8426']['nic']
        mobile = argv['Op_Admin_createNewUser_run_8426']['mobile']
        newUserId = argv['Op_Admin_createNewUser_run_8426']['newUserId']
        userName = argv['Op_Admin_createNewUser_run_8426']['userName']
        userType = argv['Op_Admin_createNewUser_run_8426']['userType']
        newSlmcReg = argv['Op_Admin_createNewUser_run_8426']['newSlmcReg']
        person_person_id = argv['Op_Admin_createNewUser_run_8426']['newPersonId']
        person_first_name = argv['Op_Admin_createNewUser_run_8426']['firstName']
        person_last_name = argv['Op_Admin_createNewUser_run_8426']['lastName']
        person_nic = argv['Op_Admin_createNewUser_run_8426']['nic']
        person_mobile = argv['Op_Admin_createNewUser_run_8426']['mobile']
        state['TABLE_person'].add({'person_id': person_person_id}, {'first_name': person_first_name,'last_name': person_last_name,'nic': person_nic,'mobile': person_mobile})
        sys_user_person_id = argv['Op_Admin_createNewUser_run_8426']['newPersonId']
        sys_user_user_id = argv['Op_Admin_createNewUser_run_8426']['newUserId']
        sys_user_user_name = argv['Op_Admin_createNewUser_run_8426']['userName']
        sys_user_user_type = argv['Op_Admin_createNewUser_run_8426']['userType']
        sys_user_password = StringVal('1234')
        state['TABLE_sys_user'].add({'user_id': sys_user_user_id}, {'person_id': sys_user_person_id,'user_name': sys_user_user_name,'user_type': sys_user_user_type,'password': sys_user_password})
        return state

    def cond6(self, state, argv):
        newPersonId = argv['Op_Admin_createNewUser_run_8426']['newPersonId']
        firstName = argv['Op_Admin_createNewUser_run_8426']['firstName']
        lastName = argv['Op_Admin_createNewUser_run_8426']['lastName']
        nic = argv['Op_Admin_createNewUser_run_8426']['nic']
        mobile = argv['Op_Admin_createNewUser_run_8426']['mobile']
        newUserId = argv['Op_Admin_createNewUser_run_8426']['newUserId']
        userName = argv['Op_Admin_createNewUser_run_8426']['userName']
        userType = argv['Op_Admin_createNewUser_run_8426']['userType']
        newLabAssistantId = argv['Op_Admin_createNewUser_run_8426']['newLabAssistantId']
        return And((argv['Op_Admin_createNewUser_run_8426']['userType'])==(StringVal('doctor')),(argv['Op_Admin_createNewUser_run_8426']['userType'])==(StringVal('lab_assistant')))

    def csop6(self, state, argv):
        return True

    def sop6(self, state, argv):
        newPersonId = argv['Op_Admin_createNewUser_run_8426']['newPersonId']
        firstName = argv['Op_Admin_createNewUser_run_8426']['firstName']
        lastName = argv['Op_Admin_createNewUser_run_8426']['lastName']
        nic = argv['Op_Admin_createNewUser_run_8426']['nic']
        mobile = argv['Op_Admin_createNewUser_run_8426']['mobile']
        newUserId = argv['Op_Admin_createNewUser_run_8426']['newUserId']
        userName = argv['Op_Admin_createNewUser_run_8426']['userName']
        userType = argv['Op_Admin_createNewUser_run_8426']['userType']
        newLabAssistantId = argv['Op_Admin_createNewUser_run_8426']['newLabAssistantId']
        person_person_id = argv['Op_Admin_createNewUser_run_8426']['newPersonId']
        person_first_name = argv['Op_Admin_createNewUser_run_8426']['firstName']
        person_last_name = argv['Op_Admin_createNewUser_run_8426']['lastName']
        person_nic = argv['Op_Admin_createNewUser_run_8426']['nic']
        person_mobile = argv['Op_Admin_createNewUser_run_8426']['mobile']
        state['TABLE_person'].add({'person_id': person_person_id}, {'first_name': person_first_name,'last_name': person_last_name,'nic': person_nic,'mobile': person_mobile})
        sys_user_person_id = argv['Op_Admin_createNewUser_run_8426']['newPersonId']
        sys_user_user_id = argv['Op_Admin_createNewUser_run_8426']['newUserId']
        sys_user_user_name = argv['Op_Admin_createNewUser_run_8426']['userName']
        sys_user_user_type = argv['Op_Admin_createNewUser_run_8426']['userType']
        sys_user_password = StringVal('1234')
        state['TABLE_sys_user'].add({'user_id': sys_user_user_id}, {'person_id': sys_user_person_id,'user_name': sys_user_user_name,'user_type': sys_user_user_type,'password': sys_user_password})
        lab_assistant_lab_assistant_id = argv['Op_Admin_createNewUser_run_8426']['newLabAssistantId']
        lab_assistant_user_id = argv['Op_Admin_createNewUser_run_8426']['newUserId']
        state['TABLE_lab_assistant'].add({'lab_assistant_id': lab_assistant_lab_assistant_id}, {'user_id': lab_assistant_user_id})
        return state

    def cond7(self, state, argv):
        newPersonId = argv['Op_Admin_createNewUser_run_8426']['newPersonId']
        firstName = argv['Op_Admin_createNewUser_run_8426']['firstName']
        lastName = argv['Op_Admin_createNewUser_run_8426']['lastName']
        nic = argv['Op_Admin_createNewUser_run_8426']['nic']
        mobile = argv['Op_Admin_createNewUser_run_8426']['mobile']
        newUserId = argv['Op_Admin_createNewUser_run_8426']['newUserId']
        userName = argv['Op_Admin_createNewUser_run_8426']['userName']
        userType = argv['Op_Admin_createNewUser_run_8426']['userType']
        newPharmacistId = argv['Op_Admin_createNewUser_run_8426']['newPharmacistId']
        return And((argv['Op_Admin_createNewUser_run_8426']['userType'])==(StringVal('doctor')),(argv['Op_Admin_createNewUser_run_8426']['userType'])==(StringVal('lab_assistant')),(argv['Op_Admin_createNewUser_run_8426']['userType'])==(StringVal('pharmacist')))

    def csop7(self, state, argv):
        return True

    def sop7(self, state, argv):
        newPersonId = argv['Op_Admin_createNewUser_run_8426']['newPersonId']
        firstName = argv['Op_Admin_createNewUser_run_8426']['firstName']
        lastName = argv['Op_Admin_createNewUser_run_8426']['lastName']
        nic = argv['Op_Admin_createNewUser_run_8426']['nic']
        mobile = argv['Op_Admin_createNewUser_run_8426']['mobile']
        newUserId = argv['Op_Admin_createNewUser_run_8426']['newUserId']
        userName = argv['Op_Admin_createNewUser_run_8426']['userName']
        userType = argv['Op_Admin_createNewUser_run_8426']['userType']
        newPharmacistId = argv['Op_Admin_createNewUser_run_8426']['newPharmacistId']
        person_person_id = argv['Op_Admin_createNewUser_run_8426']['newPersonId']
        person_first_name = argv['Op_Admin_createNewUser_run_8426']['firstName']
        person_last_name = argv['Op_Admin_createNewUser_run_8426']['lastName']
        person_nic = argv['Op_Admin_createNewUser_run_8426']['nic']
        person_mobile = argv['Op_Admin_createNewUser_run_8426']['mobile']
        state['TABLE_person'].add({'person_id': person_person_id}, {'first_name': person_first_name,'last_name': person_last_name,'nic': person_nic,'mobile': person_mobile})
        sys_user_person_id = argv['Op_Admin_createNewUser_run_8426']['newPersonId']
        sys_user_user_id = argv['Op_Admin_createNewUser_run_8426']['newUserId']
        sys_user_user_name = argv['Op_Admin_createNewUser_run_8426']['userName']
        sys_user_user_type = argv['Op_Admin_createNewUser_run_8426']['userType']
        sys_user_password = StringVal('1234')
        state['TABLE_sys_user'].add({'user_id': sys_user_user_id}, {'person_id': sys_user_person_id,'user_name': sys_user_user_name,'user_type': sys_user_user_type,'password': sys_user_password})
        pharmacist_pharmacist_id = argv['Op_Admin_createNewUser_run_8426']['newPharmacistId']
        pharmacist_user_id = argv['Op_Admin_createNewUser_run_8426']['newUserId']
        state['TABLE_pharmacist'].add({'pharmacist_id': pharmacist_pharmacist_id}, {'user_id': pharmacist_user_id})
        return state

    def cond8(self, state, argv):
        newPersonId = argv['Op_Admin_createNewUser_run_8426']['newPersonId']
        firstName = argv['Op_Admin_createNewUser_run_8426']['firstName']
        lastName = argv['Op_Admin_createNewUser_run_8426']['lastName']
        nic = argv['Op_Admin_createNewUser_run_8426']['nic']
        mobile = argv['Op_Admin_createNewUser_run_8426']['mobile']
        newUserId = argv['Op_Admin_createNewUser_run_8426']['newUserId']
        userName = argv['Op_Admin_createNewUser_run_8426']['userName']
        userType = argv['Op_Admin_createNewUser_run_8426']['userType']
        newSlmcReg = argv['Op_Admin_createNewUser_run_8426']['newSlmcReg']
        return (argv['Op_Admin_createNewUser_run_8426']['userType'])==(StringVal('doctor'))

    def csop8(self, state, argv):
        return True

    def sop8(self, state, argv):
        newPersonId = argv['Op_Admin_createNewUser_run_8426']['newPersonId']
        firstName = argv['Op_Admin_createNewUser_run_8426']['firstName']
        lastName = argv['Op_Admin_createNewUser_run_8426']['lastName']
        nic = argv['Op_Admin_createNewUser_run_8426']['nic']
        mobile = argv['Op_Admin_createNewUser_run_8426']['mobile']
        newUserId = argv['Op_Admin_createNewUser_run_8426']['newUserId']
        userName = argv['Op_Admin_createNewUser_run_8426']['userName']
        userType = argv['Op_Admin_createNewUser_run_8426']['userType']
        newSlmcReg = argv['Op_Admin_createNewUser_run_8426']['newSlmcReg']
        person_person_id = argv['Op_Admin_createNewUser_run_8426']['newPersonId']
        person_first_name = argv['Op_Admin_createNewUser_run_8426']['firstName']
        person_last_name = argv['Op_Admin_createNewUser_run_8426']['lastName']
        person_nic = argv['Op_Admin_createNewUser_run_8426']['nic']
        person_mobile = argv['Op_Admin_createNewUser_run_8426']['mobile']
        state['TABLE_person'].add({'person_id': person_person_id}, {'first_name': person_first_name,'last_name': person_last_name,'nic': person_nic,'mobile': person_mobile})
        sys_user_person_id = argv['Op_Admin_createNewUser_run_8426']['newPersonId']
        sys_user_user_id = argv['Op_Admin_createNewUser_run_8426']['newUserId']
        sys_user_user_name = argv['Op_Admin_createNewUser_run_8426']['userName']
        sys_user_user_type = argv['Op_Admin_createNewUser_run_8426']['userType']
        sys_user_password = StringVal('1234')
        state['TABLE_sys_user'].add({'user_id': sys_user_user_id}, {'person_id': sys_user_person_id,'user_name': sys_user_user_name,'user_type': sys_user_user_type,'password': sys_user_password})
        doctor_slmc_reg_no = argv['Op_Admin_createNewUser_run_8426']['newSlmcReg']
        doctor_user_id = argv['Op_Admin_createNewUser_run_8426']['newUserId']
        state['TABLE_doctor'].add({'slmc_reg_no': doctor_slmc_reg_no}, {'user_id': doctor_user_id})
        return state


class Op_Pharmacist_bill_run_8427():
    def __init__(self):
        self.sops = [(self.cond0, self.csop0, self.sop0)]
        self.axiom = AxiomEmpty()

    def cond0(self, state, argv):
        id = argv['Op_Pharmacist_bill_run_8427']['id']
        tmp_bill_tmp_bill_id = argv['Op_Pharmacist_bill_run_8427']['tmp_bill_tmp_bill_id']
        return And((state['TABLE_tmp_bill'].notNil({'patient_id': argv['Op_Pharmacist_bill_run_8427']['id']}) == True),(state['TABLE_tmp_bill'].notNil({'tmp_bill_id': state['TABLE_tmp_bill'].get({'patient_id': argv['Op_Pharmacist_bill_run_8427']['id']}, 'tmp_bill_id')}) == True))

    def csop0(self, state, argv):
        return True

    def sop0(self, state, argv):
        id = argv['Op_Pharmacist_bill_run_8427']['id']
        tmp_bill_tmp_bill_id = argv['Op_Pharmacist_bill_run_8427']['tmp_bill_tmp_bill_id']
        tmp_bill_tmp_bill_id = state['TABLE_tmp_bill'].get({'tmp_bill_id': state['TABLE_tmp_bill'].get({'patient_id': argv['Op_Pharmacist_bill_run_8427']['id']}, 'tmp_bill_id')}, 'tmp_bill_id')
        tmp_bill_doctor_fee = state['TABLE_tmp_bill'].get({'tmp_bill_id': state['TABLE_tmp_bill'].get({'patient_id': argv['Op_Pharmacist_bill_run_8427']['id']}, 'tmp_bill_id')}, 'doctor_fee')
        tmp_bill_hospital_fee = state['TABLE_tmp_bill'].get({'tmp_bill_id': state['TABLE_tmp_bill'].get({'patient_id': argv['Op_Pharmacist_bill_run_8427']['id']}, 'tmp_bill_id')}, 'hospital_fee')
        tmp_bill_pharmacy_fee = state['TABLE_tmp_bill'].get({'tmp_bill_id': state['TABLE_tmp_bill'].get({'patient_id': argv['Op_Pharmacist_bill_run_8427']['id']}, 'tmp_bill_id')}, 'pharmacy_fee')
        tmp_bill_laboratory_fee = state['TABLE_tmp_bill'].get({'tmp_bill_id': state['TABLE_tmp_bill'].get({'patient_id': argv['Op_Pharmacist_bill_run_8427']['id']}, 'tmp_bill_id')}, 'laboratory_fee')
        tmp_bill_appointment_fee = state['TABLE_tmp_bill'].get({'tmp_bill_id': state['TABLE_tmp_bill'].get({'patient_id': argv['Op_Pharmacist_bill_run_8427']['id']}, 'tmp_bill_id')}, 'appointment_fee')
        tmp_bill_vat = state['TABLE_tmp_bill'].get({'tmp_bill_id': state['TABLE_tmp_bill'].get({'patient_id': argv['Op_Pharmacist_bill_run_8427']['id']}, 'tmp_bill_id')}, 'vat')
        tmp_bill_discount = state['TABLE_tmp_bill'].get({'tmp_bill_id': state['TABLE_tmp_bill'].get({'patient_id': argv['Op_Pharmacist_bill_run_8427']['id']}, 'tmp_bill_id')}, 'discount')
        tmp_bill_consultant_id = state['TABLE_tmp_bill'].get({'tmp_bill_id': state['TABLE_tmp_bill'].get({'patient_id': argv['Op_Pharmacist_bill_run_8427']['id']}, 'tmp_bill_id')}, 'consultant_id')
        tmp_bill_patient_id = state['TABLE_tmp_bill'].get({'tmp_bill_id': state['TABLE_tmp_bill'].get({'patient_id': argv['Op_Pharmacist_bill_run_8427']['id']}, 'tmp_bill_id')}, 'patient_id')
        tmp_bill_laboratory_fee = 100
        state['TABLE_tmp_bill'].update({'tmp_bill_id': state['TABLE_tmp_bill'].get({'patient_id': argv['Op_Pharmacist_bill_run_8427']['id']}, 'tmp_bill_id')}, {'tmp_bill_id': tmp_bill_tmp_bill_id, 'doctor_fee': tmp_bill_doctor_fee, 'hospital_fee': tmp_bill_hospital_fee, 'pharmacy_fee': tmp_bill_pharmacy_fee, 'laboratory_fee': tmp_bill_laboratory_fee, 'appointment_fee': tmp_bill_appointment_fee, 'vat': tmp_bill_vat, 'discount': tmp_bill_discount, 'consultant_id': tmp_bill_consultant_id, 'patient_id': tmp_bill_patient_id})
        return state


class Op_Receptionist_updatePatientInfo_run_8428():
    def __init__(self):
        self.sops = [(self.cond0, self.csop0, self.sop0)]
        self.axiom = AxiomEmpty()

    def cond0(self, state, argv):
        patientId = argv['Op_Receptionist_updatePatientInfo_run_8428']['patientId']
        info = argv['Op_Receptionist_updatePatientInfo_run_8428']['info']
        patient_patient_id = argv['Op_Receptionist_updatePatientInfo_run_8428']['patient_patient_id']
        return And((state['TABLE_patient'].notNil({'patient_id': argv['Op_Receptionist_updatePatientInfo_run_8428']['patientId']}) == True),(state['TABLE_patient'].notNil({'patient_id': argv['Op_Receptionist_updatePatientInfo_run_8428']['patientId']}) == True))

    def csop0(self, state, argv):
        return True

    def sop0(self, state, argv):
        patientId = argv['Op_Receptionist_updatePatientInfo_run_8428']['patientId']
        info = argv['Op_Receptionist_updatePatientInfo_run_8428']['info']
        patient_patient_id = argv['Op_Receptionist_updatePatientInfo_run_8428']['patient_patient_id']
        patient_patient_id = state['TABLE_patient'].get({'patient_id': argv['Op_Receptionist_updatePatientInfo_run_8428']['patientId']}, 'patient_id')
        patient_person_id = state['TABLE_patient'].get({'patient_id': argv['Op_Receptionist_updatePatientInfo_run_8428']['patientId']}, 'person_id')
        patient_drug_allergies_and_reactions = state['TABLE_patient'].get({'patient_id': argv['Op_Receptionist_updatePatientInfo_run_8428']['patientId']}, 'drug_allergies_and_reactions')
        patient_drug_allergies_and_reactions = argv['Op_Receptionist_updatePatientInfo_run_8428']['info']
        state['TABLE_patient'].update({'patient_id': argv['Op_Receptionist_updatePatientInfo_run_8428']['patientId']}, {'patient_id': patient_patient_id, 'person_id': patient_person_id, 'drug_allergies_and_reactions': patient_drug_allergies_and_reactions})
        return state


class Op_Doctor_updateDoctorInfo_run_8429():
    def __init__(self):
        self.sops = [(self.cond0, self.csop0, self.sop0)]
        self.axiom = AxiomEmpty()

    def cond0(self, state, argv):
        id = argv['Op_Doctor_updateDoctorInfo_run_8429']['id']
        doctor_slmc_reg_no = argv['Op_Doctor_updateDoctorInfo_run_8429']['doctor_slmc_reg_no']
        return (state['TABLE_doctor'].notNil({'slmc_reg_no': argv['Op_Doctor_updateDoctorInfo_run_8429']['id']}) == True)

    def csop0(self, state, argv):
        return True

    def sop0(self, state, argv):
        id = argv['Op_Doctor_updateDoctorInfo_run_8429']['id']
        doctor_slmc_reg_no = argv['Op_Doctor_updateDoctorInfo_run_8429']['doctor_slmc_reg_no']
        doctor_slmc_reg_no = state['TABLE_doctor'].get({'slmc_reg_no': argv['Op_Doctor_updateDoctorInfo_run_8429']['id']}, 'slmc_reg_no')
        doctor_user_id = state['TABLE_doctor'].get({'slmc_reg_no': argv['Op_Doctor_updateDoctorInfo_run_8429']['id']}, 'user_id')
        doctor_education = state['TABLE_doctor'].get({'slmc_reg_no': argv['Op_Doctor_updateDoctorInfo_run_8429']['id']}, 'education')
        doctor_training = state['TABLE_doctor'].get({'slmc_reg_no': argv['Op_Doctor_updateDoctorInfo_run_8429']['id']}, 'training')
        doctor_experienced_areas = state['TABLE_doctor'].get({'slmc_reg_no': argv['Op_Doctor_updateDoctorInfo_run_8429']['id']}, 'experienced_areas')
        doctor_experience = state['TABLE_doctor'].get({'slmc_reg_no': argv['Op_Doctor_updateDoctorInfo_run_8429']['id']}, 'experience')
        doctor_achievements = state['TABLE_doctor'].get({'slmc_reg_no': argv['Op_Doctor_updateDoctorInfo_run_8429']['id']}, 'achievements')
        doctor_channelling_fee = state['TABLE_doctor'].get({'slmc_reg_no': argv['Op_Doctor_updateDoctorInfo_run_8429']['id']}, 'channelling_fee')
        doctor_achievements = argv['Op_Doctor_updateDoctorInfo_run_8429']['id']
        state['TABLE_doctor'].update({'slmc_reg_no': argv['Op_Doctor_updateDoctorInfo_run_8429']['id']}, {'slmc_reg_no': doctor_slmc_reg_no, 'user_id': doctor_user_id, 'education': doctor_education, 'training': doctor_training, 'experienced_areas': doctor_experienced_areas, 'experience': doctor_experience, 'achievements': doctor_achievements, 'channelling_fee': doctor_channelling_fee})
        return state


class Op_Receptionist_updateProfileInfo_run_8430():
    def __init__(self):
        self.sops = [(self.cond0, self.csop0, self.sop0)]
        self.axiom = AxiomEmpty()

    def cond0(self, state, argv):
        userId = argv['Op_Receptionist_updateProfileInfo_run_8430']['userId']
        address = argv['Op_Receptionist_updateProfileInfo_run_8430']['address']
        sys_user_person_id = argv['Op_Receptionist_updateProfileInfo_run_8430']['sys_user_person_id']
        person_person_id = argv['Op_Receptionist_updateProfileInfo_run_8430']['person_person_id']
        return And((state['TABLE_sys_user'].notNil({'user_id': argv['Op_Receptionist_updateProfileInfo_run_8430']['userId']}) == True),(state['TABLE_person'].notNil({'person_id': state['TABLE_sys_user'].get({'user_id': argv['Op_Receptionist_updateProfileInfo_run_8430']['userId']}, 'person_id')}) == True))

    def csop0(self, state, argv):
        return True

    def sop0(self, state, argv):
        userId = argv['Op_Receptionist_updateProfileInfo_run_8430']['userId']
        address = argv['Op_Receptionist_updateProfileInfo_run_8430']['address']
        sys_user_person_id = argv['Op_Receptionist_updateProfileInfo_run_8430']['sys_user_person_id']
        person_person_id = argv['Op_Receptionist_updateProfileInfo_run_8430']['person_person_id']
        person_person_id = state['TABLE_person'].get({'person_id': state['TABLE_sys_user'].get({'user_id': argv['Op_Receptionist_updateProfileInfo_run_8430']['userId']}, 'person_id')}, 'person_id')
        person_user_id = state['TABLE_person'].get({'person_id': state['TABLE_sys_user'].get({'user_id': argv['Op_Receptionist_updateProfileInfo_run_8430']['userId']}, 'person_id')}, 'user_id')
        person_nic = state['TABLE_person'].get({'person_id': state['TABLE_sys_user'].get({'user_id': argv['Op_Receptionist_updateProfileInfo_run_8430']['userId']}, 'person_id')}, 'nic')
        person_gender = state['TABLE_person'].get({'person_id': state['TABLE_sys_user'].get({'user_id': argv['Op_Receptionist_updateProfileInfo_run_8430']['userId']}, 'person_id')}, 'gender')
        person_date_of_birth = state['TABLE_person'].get({'person_id': state['TABLE_sys_user'].get({'user_id': argv['Op_Receptionist_updateProfileInfo_run_8430']['userId']}, 'person_id')}, 'date_of_birth')
        person_address = state['TABLE_person'].get({'person_id': state['TABLE_sys_user'].get({'user_id': argv['Op_Receptionist_updateProfileInfo_run_8430']['userId']}, 'person_id')}, 'address')
        person_mobile = state['TABLE_person'].get({'person_id': state['TABLE_sys_user'].get({'user_id': argv['Op_Receptionist_updateProfileInfo_run_8430']['userId']}, 'person_id')}, 'mobile')
        person_first_name = state['TABLE_person'].get({'person_id': state['TABLE_sys_user'].get({'user_id': argv['Op_Receptionist_updateProfileInfo_run_8430']['userId']}, 'person_id')}, 'first_name')
        person_last_name = state['TABLE_person'].get({'person_id': state['TABLE_sys_user'].get({'user_id': argv['Op_Receptionist_updateProfileInfo_run_8430']['userId']}, 'person_id')}, 'last_name')
        person_email = state['TABLE_person'].get({'person_id': state['TABLE_sys_user'].get({'user_id': argv['Op_Receptionist_updateProfileInfo_run_8430']['userId']}, 'person_id')}, 'email')
        person_nationality = state['TABLE_person'].get({'person_id': state['TABLE_sys_user'].get({'user_id': argv['Op_Receptionist_updateProfileInfo_run_8430']['userId']}, 'person_id')}, 'nationality')
        person_religion = state['TABLE_person'].get({'person_id': state['TABLE_sys_user'].get({'user_id': argv['Op_Receptionist_updateProfileInfo_run_8430']['userId']}, 'person_id')}, 'religion')
        person_address = argv['Op_Receptionist_updateProfileInfo_run_8430']['address']
        state['TABLE_person'].update({'person_id': state['TABLE_sys_user'].get({'user_id': argv['Op_Receptionist_updateProfileInfo_run_8430']['userId']}, 'person_id')}, {'person_id': person_person_id, 'user_id': person_user_id, 'nic': person_nic, 'gender': person_gender, 'date_of_birth': person_date_of_birth, 'address': person_address, 'mobile': person_mobile, 'first_name': person_first_name, 'last_name': person_last_name, 'email': person_email, 'nationality': person_nationality, 'religion': person_religion})
        return state


class Op_LabAssistant_SeriumCreatinePhosphokinaseTotal_run_8431():
    def __init__(self):
        self.sops = [(self.cond0, self.csop0, self.sop0)]
        self.axiom = AxiomEmpty()

    def cond0(self, state, argv):
        newTstId = argv['Op_LabAssistant_SeriumCreatinePhosphokinaseTotal_run_8431']['newTstId']
        appId = argv['Op_LabAssistant_SeriumCreatinePhosphokinaseTotal_run_8431']['appId']
        cpkTotal = argv['Op_LabAssistant_SeriumCreatinePhosphokinaseTotal_run_8431']['cpkTotal']
        now = argv['Op_LabAssistant_SeriumCreatinePhosphokinaseTotal_run_8431']['now']
        return (state['TABLE_SeriumCreatinePhosphokinaseTotal'].notNil({'tst_SCPT_id': argv['Op_LabAssistant_SeriumCreatinePhosphokinaseTotal_run_8431']['newTstId']}) == False)

    def csop0(self, state, argv):
        return True

    def sop0(self, state, argv):
        newTstId = argv['Op_LabAssistant_SeriumCreatinePhosphokinaseTotal_run_8431']['newTstId']
        appId = argv['Op_LabAssistant_SeriumCreatinePhosphokinaseTotal_run_8431']['appId']
        cpkTotal = argv['Op_LabAssistant_SeriumCreatinePhosphokinaseTotal_run_8431']['cpkTotal']
        now = argv['Op_LabAssistant_SeriumCreatinePhosphokinaseTotal_run_8431']['now']
        SeriumCreatinePhosphokinaseTotal_tst_SCPT_id = argv['Op_LabAssistant_SeriumCreatinePhosphokinaseTotal_run_8431']['newTstId']
        SeriumCreatinePhosphokinaseTotal_appointment_id = argv['Op_LabAssistant_SeriumCreatinePhosphokinaseTotal_run_8431']['appId']
        SeriumCreatinePhosphokinaseTotal_cpkTotal = argv['Op_LabAssistant_SeriumCreatinePhosphokinaseTotal_run_8431']['cpkTotal']
        SeriumCreatinePhosphokinaseTotal_date = argv['Op_LabAssistant_SeriumCreatinePhosphokinaseTotal_run_8431']['now']
        state['TABLE_SeriumCreatinePhosphokinaseTotal'].add({'tst_SCPT_id': SeriumCreatinePhosphokinaseTotal_tst_SCPT_id}, {'appointment_id': SeriumCreatinePhosphokinaseTotal_appointment_id,'cpkTotal': SeriumCreatinePhosphokinaseTotal_cpkTotal,'date': SeriumCreatinePhosphokinaseTotal_date})
        return state


class Op_Cashier_updateAccountInfo_run_8432():
    def __init__(self):
        self.sops = [(self.cond0, self.csop0, self.sop0)]
        self.axiom = AxiomEmpty()

    def cond0(self, state, argv):
        id = argv['Op_Cashier_updateAccountInfo_run_8432']['id']
        sys_user_user_id = argv['Op_Cashier_updateAccountInfo_run_8432']['sys_user_user_id']
        return (state['TABLE_sys_user'].notNil({'user_id': argv['Op_Cashier_updateAccountInfo_run_8432']['id']}) == True)

    def csop0(self, state, argv):
        return True

    def sop0(self, state, argv):
        id = argv['Op_Cashier_updateAccountInfo_run_8432']['id']
        sys_user_user_id = argv['Op_Cashier_updateAccountInfo_run_8432']['sys_user_user_id']
        sys_user_person_id = state['TABLE_sys_user'].get({'user_id': argv['Op_Cashier_updateAccountInfo_run_8432']['id']}, 'person_id')
        sys_user_user_id = state['TABLE_sys_user'].get({'user_id': argv['Op_Cashier_updateAccountInfo_run_8432']['id']}, 'user_id')
        sys_user_user_name = state['TABLE_sys_user'].get({'user_id': argv['Op_Cashier_updateAccountInfo_run_8432']['id']}, 'user_name')
        sys_user_user_type = state['TABLE_sys_user'].get({'user_id': argv['Op_Cashier_updateAccountInfo_run_8432']['id']}, 'user_type')
        sys_user_other_info = state['TABLE_sys_user'].get({'user_id': argv['Op_Cashier_updateAccountInfo_run_8432']['id']}, 'other_info')
        sys_user_password = state['TABLE_sys_user'].get({'user_id': argv['Op_Cashier_updateAccountInfo_run_8432']['id']}, 'password')
        sys_user_online = state['TABLE_sys_user'].get({'user_id': argv['Op_Cashier_updateAccountInfo_run_8432']['id']}, 'online')
        sys_user_login = state['TABLE_sys_user'].get({'user_id': argv['Op_Cashier_updateAccountInfo_run_8432']['id']}, 'login')
        sys_user_logout = state['TABLE_sys_user'].get({'user_id': argv['Op_Cashier_updateAccountInfo_run_8432']['id']}, 'logout')
        sys_user_profile_pic = state['TABLE_sys_user'].get({'user_id': argv['Op_Cashier_updateAccountInfo_run_8432']['id']}, 'profile_pic')
        sys_user_suspend = state['TABLE_sys_user'].get({'user_id': argv['Op_Cashier_updateAccountInfo_run_8432']['id']}, 'suspend')
        sys_user_other_info = argv['Op_Cashier_updateAccountInfo_run_8432']['id']
        state['TABLE_sys_user'].update({'user_id': argv['Op_Cashier_updateAccountInfo_run_8432']['id']}, {'person_id': sys_user_person_id, 'user_id': sys_user_user_id, 'user_name': sys_user_user_name, 'user_type': sys_user_user_type, 'other_info': sys_user_other_info, 'password': sys_user_password, 'online': sys_user_online, 'login': sys_user_login, 'logout': sys_user_logout, 'profile_pic': sys_user_profile_pic, 'suspend': sys_user_suspend})
        return state


class Op_Admin_suspendUser_run_8433():
    def __init__(self):
        self.sops = [(self.cond0, self.csop0, self.sop0)]
        self.axiom = AxiomEmpty()

    def cond0(self, state, argv):
        id = argv['Op_Admin_suspendUser_run_8433']['id']
        sys_user_user_id = argv['Op_Admin_suspendUser_run_8433']['sys_user_user_id']
        return (state['TABLE_sys_user'].notNil({'user_id': argv['Op_Admin_suspendUser_run_8433']['id']}) == True)

    def csop0(self, state, argv):
        return True

    def sop0(self, state, argv):
        id = argv['Op_Admin_suspendUser_run_8433']['id']
        sys_user_user_id = argv['Op_Admin_suspendUser_run_8433']['sys_user_user_id']
        sys_user_person_id = state['TABLE_sys_user'].get({'user_id': argv['Op_Admin_suspendUser_run_8433']['id']}, 'person_id')
        sys_user_user_id = state['TABLE_sys_user'].get({'user_id': argv['Op_Admin_suspendUser_run_8433']['id']}, 'user_id')
        sys_user_user_name = state['TABLE_sys_user'].get({'user_id': argv['Op_Admin_suspendUser_run_8433']['id']}, 'user_name')
        sys_user_user_type = state['TABLE_sys_user'].get({'user_id': argv['Op_Admin_suspendUser_run_8433']['id']}, 'user_type')
        sys_user_other_info = state['TABLE_sys_user'].get({'user_id': argv['Op_Admin_suspendUser_run_8433']['id']}, 'other_info')
        sys_user_password = state['TABLE_sys_user'].get({'user_id': argv['Op_Admin_suspendUser_run_8433']['id']}, 'password')
        sys_user_online = state['TABLE_sys_user'].get({'user_id': argv['Op_Admin_suspendUser_run_8433']['id']}, 'online')
        sys_user_login = state['TABLE_sys_user'].get({'user_id': argv['Op_Admin_suspendUser_run_8433']['id']}, 'login')
        sys_user_logout = state['TABLE_sys_user'].get({'user_id': argv['Op_Admin_suspendUser_run_8433']['id']}, 'logout')
        sys_user_profile_pic = state['TABLE_sys_user'].get({'user_id': argv['Op_Admin_suspendUser_run_8433']['id']}, 'profile_pic')
        sys_user_suspend = state['TABLE_sys_user'].get({'user_id': argv['Op_Admin_suspendUser_run_8433']['id']}, 'suspend')
        sys_user_suspend = 1
        state['TABLE_sys_user'].update({'user_id': argv['Op_Admin_suspendUser_run_8433']['id']}, {'person_id': sys_user_person_id, 'user_id': sys_user_user_id, 'user_name': sys_user_user_name, 'user_type': sys_user_user_type, 'other_info': sys_user_other_info, 'password': sys_user_password, 'online': sys_user_online, 'login': sys_user_login, 'logout': sys_user_logout, 'profile_pic': sys_user_profile_pic, 'suspend': sys_user_suspend})
        return state


class Op_Doctor_updateProfileInfo_run_8434():
    def __init__(self):
        self.sops = [(self.cond0, self.csop0, self.sop0)]
        self.axiom = AxiomEmpty()

    def cond0(self, state, argv):
        id = argv['Op_Doctor_updateProfileInfo_run_8434']['id']
        doctor_user_id = argv['Op_Doctor_updateProfileInfo_run_8434']['doctor_user_id']
        sys_user_person_id = argv['Op_Doctor_updateProfileInfo_run_8434']['sys_user_person_id']
        person_person_id = argv['Op_Doctor_updateProfileInfo_run_8434']['person_person_id']
        return And((state['TABLE_doctor'].notNil({'slmc_reg_no': argv['Op_Doctor_updateProfileInfo_run_8434']['id']}) == True),(state['TABLE_sys_user'].notNil({'user_id': state['TABLE_doctor'].get({'slmc_reg_no': argv['Op_Doctor_updateProfileInfo_run_8434']['id']}, 'user_id')}) == True),(state['TABLE_person'].notNil({'person_id': state['TABLE_sys_user'].get({'user_id': state['TABLE_doctor'].get({'slmc_reg_no': argv['Op_Doctor_updateProfileInfo_run_8434']['id']}, 'user_id')}, 'person_id')}) == True))

    def csop0(self, state, argv):
        return True

    def sop0(self, state, argv):
        id = argv['Op_Doctor_updateProfileInfo_run_8434']['id']
        doctor_user_id = argv['Op_Doctor_updateProfileInfo_run_8434']['doctor_user_id']
        sys_user_person_id = argv['Op_Doctor_updateProfileInfo_run_8434']['sys_user_person_id']
        person_person_id = argv['Op_Doctor_updateProfileInfo_run_8434']['person_person_id']
        person_person_id = state['TABLE_person'].get({'person_id': state['TABLE_sys_user'].get({'user_id': state['TABLE_doctor'].get({'slmc_reg_no': argv['Op_Doctor_updateProfileInfo_run_8434']['id']}, 'user_id')}, 'person_id')}, 'person_id')
        person_user_id = state['TABLE_person'].get({'person_id': state['TABLE_sys_user'].get({'user_id': state['TABLE_doctor'].get({'slmc_reg_no': argv['Op_Doctor_updateProfileInfo_run_8434']['id']}, 'user_id')}, 'person_id')}, 'user_id')
        person_nic = state['TABLE_person'].get({'person_id': state['TABLE_sys_user'].get({'user_id': state['TABLE_doctor'].get({'slmc_reg_no': argv['Op_Doctor_updateProfileInfo_run_8434']['id']}, 'user_id')}, 'person_id')}, 'nic')
        person_gender = state['TABLE_person'].get({'person_id': state['TABLE_sys_user'].get({'user_id': state['TABLE_doctor'].get({'slmc_reg_no': argv['Op_Doctor_updateProfileInfo_run_8434']['id']}, 'user_id')}, 'person_id')}, 'gender')
        person_date_of_birth = state['TABLE_person'].get({'person_id': state['TABLE_sys_user'].get({'user_id': state['TABLE_doctor'].get({'slmc_reg_no': argv['Op_Doctor_updateProfileInfo_run_8434']['id']}, 'user_id')}, 'person_id')}, 'date_of_birth')
        person_address = state['TABLE_person'].get({'person_id': state['TABLE_sys_user'].get({'user_id': state['TABLE_doctor'].get({'slmc_reg_no': argv['Op_Doctor_updateProfileInfo_run_8434']['id']}, 'user_id')}, 'person_id')}, 'address')
        person_mobile = state['TABLE_person'].get({'person_id': state['TABLE_sys_user'].get({'user_id': state['TABLE_doctor'].get({'slmc_reg_no': argv['Op_Doctor_updateProfileInfo_run_8434']['id']}, 'user_id')}, 'person_id')}, 'mobile')
        person_first_name = state['TABLE_person'].get({'person_id': state['TABLE_sys_user'].get({'user_id': state['TABLE_doctor'].get({'slmc_reg_no': argv['Op_Doctor_updateProfileInfo_run_8434']['id']}, 'user_id')}, 'person_id')}, 'first_name')
        person_last_name = state['TABLE_person'].get({'person_id': state['TABLE_sys_user'].get({'user_id': state['TABLE_doctor'].get({'slmc_reg_no': argv['Op_Doctor_updateProfileInfo_run_8434']['id']}, 'user_id')}, 'person_id')}, 'last_name')
        person_email = state['TABLE_person'].get({'person_id': state['TABLE_sys_user'].get({'user_id': state['TABLE_doctor'].get({'slmc_reg_no': argv['Op_Doctor_updateProfileInfo_run_8434']['id']}, 'user_id')}, 'person_id')}, 'email')
        person_nationality = state['TABLE_person'].get({'person_id': state['TABLE_sys_user'].get({'user_id': state['TABLE_doctor'].get({'slmc_reg_no': argv['Op_Doctor_updateProfileInfo_run_8434']['id']}, 'user_id')}, 'person_id')}, 'nationality')
        person_religion = state['TABLE_person'].get({'person_id': state['TABLE_sys_user'].get({'user_id': state['TABLE_doctor'].get({'slmc_reg_no': argv['Op_Doctor_updateProfileInfo_run_8434']['id']}, 'user_id')}, 'person_id')}, 'religion')
        person_address = argv['Op_Doctor_updateProfileInfo_run_8434']['id']
        state['TABLE_person'].update({'person_id': state['TABLE_sys_user'].get({'user_id': state['TABLE_doctor'].get({'slmc_reg_no': argv['Op_Doctor_updateProfileInfo_run_8434']['id']}, 'user_id')}, 'person_id')}, {'person_id': person_person_id, 'user_id': person_user_id, 'nic': person_nic, 'gender': person_gender, 'date_of_birth': person_date_of_birth, 'address': person_address, 'mobile': person_mobile, 'first_name': person_first_name, 'last_name': person_last_name, 'email': person_email, 'nationality': person_nationality, 'religion': person_religion})
        return state


class Op_Pharmacist_updateProfileInfo_run_8435():
    def __init__(self):
        self.sops = [(self.cond0, self.csop0, self.sop0)]
        self.axiom = AxiomEmpty()

    def cond0(self, state, argv):
        id = argv['Op_Pharmacist_updateProfileInfo_run_8435']['id']
        address = argv['Op_Pharmacist_updateProfileInfo_run_8435']['address']
        sys_user_person_id = argv['Op_Pharmacist_updateProfileInfo_run_8435']['sys_user_person_id']
        person_person_id = argv['Op_Pharmacist_updateProfileInfo_run_8435']['person_person_id']
        return And((state['TABLE_sys_user'].notNil({'user_id': argv['Op_Pharmacist_updateProfileInfo_run_8435']['id']}) == True),(state['TABLE_person'].notNil({'person_id': state['TABLE_sys_user'].get({'user_id': argv['Op_Pharmacist_updateProfileInfo_run_8435']['id']}, 'person_id')}) == True))

    def csop0(self, state, argv):
        return True

    def sop0(self, state, argv):
        id = argv['Op_Pharmacist_updateProfileInfo_run_8435']['id']
        address = argv['Op_Pharmacist_updateProfileInfo_run_8435']['address']
        sys_user_person_id = argv['Op_Pharmacist_updateProfileInfo_run_8435']['sys_user_person_id']
        person_person_id = argv['Op_Pharmacist_updateProfileInfo_run_8435']['person_person_id']
        person_person_id = state['TABLE_person'].get({'person_id': state['TABLE_sys_user'].get({'user_id': argv['Op_Pharmacist_updateProfileInfo_run_8435']['id']}, 'person_id')}, 'person_id')
        person_user_id = state['TABLE_person'].get({'person_id': state['TABLE_sys_user'].get({'user_id': argv['Op_Pharmacist_updateProfileInfo_run_8435']['id']}, 'person_id')}, 'user_id')
        person_nic = state['TABLE_person'].get({'person_id': state['TABLE_sys_user'].get({'user_id': argv['Op_Pharmacist_updateProfileInfo_run_8435']['id']}, 'person_id')}, 'nic')
        person_gender = state['TABLE_person'].get({'person_id': state['TABLE_sys_user'].get({'user_id': argv['Op_Pharmacist_updateProfileInfo_run_8435']['id']}, 'person_id')}, 'gender')
        person_date_of_birth = state['TABLE_person'].get({'person_id': state['TABLE_sys_user'].get({'user_id': argv['Op_Pharmacist_updateProfileInfo_run_8435']['id']}, 'person_id')}, 'date_of_birth')
        person_address = state['TABLE_person'].get({'person_id': state['TABLE_sys_user'].get({'user_id': argv['Op_Pharmacist_updateProfileInfo_run_8435']['id']}, 'person_id')}, 'address')
        person_mobile = state['TABLE_person'].get({'person_id': state['TABLE_sys_user'].get({'user_id': argv['Op_Pharmacist_updateProfileInfo_run_8435']['id']}, 'person_id')}, 'mobile')
        person_first_name = state['TABLE_person'].get({'person_id': state['TABLE_sys_user'].get({'user_id': argv['Op_Pharmacist_updateProfileInfo_run_8435']['id']}, 'person_id')}, 'first_name')
        person_last_name = state['TABLE_person'].get({'person_id': state['TABLE_sys_user'].get({'user_id': argv['Op_Pharmacist_updateProfileInfo_run_8435']['id']}, 'person_id')}, 'last_name')
        person_email = state['TABLE_person'].get({'person_id': state['TABLE_sys_user'].get({'user_id': argv['Op_Pharmacist_updateProfileInfo_run_8435']['id']}, 'person_id')}, 'email')
        person_nationality = state['TABLE_person'].get({'person_id': state['TABLE_sys_user'].get({'user_id': argv['Op_Pharmacist_updateProfileInfo_run_8435']['id']}, 'person_id')}, 'nationality')
        person_religion = state['TABLE_person'].get({'person_id': state['TABLE_sys_user'].get({'user_id': argv['Op_Pharmacist_updateProfileInfo_run_8435']['id']}, 'person_id')}, 'religion')
        person_address = argv['Op_Pharmacist_updateProfileInfo_run_8435']['address']
        state['TABLE_person'].update({'person_id': state['TABLE_sys_user'].get({'user_id': argv['Op_Pharmacist_updateProfileInfo_run_8435']['id']}, 'person_id')}, {'person_id': person_person_id, 'user_id': person_user_id, 'nic': person_nic, 'gender': person_gender, 'date_of_birth': person_date_of_birth, 'address': person_address, 'mobile': person_mobile, 'first_name': person_first_name, 'last_name': person_last_name, 'email': person_email, 'nationality': person_nationality, 'religion': person_religion})
        return state


class Op_Doctor_bill_run_8436():
    def __init__(self):
        self.sops = [(self.cond0, self.csop0, self.sop0)]
        self.axiom = AxiomEmpty()

    def cond0(self, state, argv):
        id = argv['Op_Doctor_bill_run_8436']['id']
        tmp_bill_tmp_bill_id = argv['Op_Doctor_bill_run_8436']['tmp_bill_tmp_bill_id']
        return And((state['TABLE_tmp_bill'].notNil({'patient_id': argv['Op_Doctor_bill_run_8436']['id']}) == True),(state['TABLE_tmp_bill'].notNil({'tmp_bill_id': state['TABLE_tmp_bill'].get({'patient_id': argv['Op_Doctor_bill_run_8436']['id']}, 'tmp_bill_id')}) == True))

    def csop0(self, state, argv):
        return True

    def sop0(self, state, argv):
        id = argv['Op_Doctor_bill_run_8436']['id']
        tmp_bill_tmp_bill_id = argv['Op_Doctor_bill_run_8436']['tmp_bill_tmp_bill_id']
        tmp_bill_tmp_bill_id = state['TABLE_tmp_bill'].get({'tmp_bill_id': state['TABLE_tmp_bill'].get({'patient_id': argv['Op_Doctor_bill_run_8436']['id']}, 'tmp_bill_id')}, 'tmp_bill_id')
        tmp_bill_doctor_fee = state['TABLE_tmp_bill'].get({'tmp_bill_id': state['TABLE_tmp_bill'].get({'patient_id': argv['Op_Doctor_bill_run_8436']['id']}, 'tmp_bill_id')}, 'doctor_fee')
        tmp_bill_hospital_fee = state['TABLE_tmp_bill'].get({'tmp_bill_id': state['TABLE_tmp_bill'].get({'patient_id': argv['Op_Doctor_bill_run_8436']['id']}, 'tmp_bill_id')}, 'hospital_fee')
        tmp_bill_pharmacy_fee = state['TABLE_tmp_bill'].get({'tmp_bill_id': state['TABLE_tmp_bill'].get({'patient_id': argv['Op_Doctor_bill_run_8436']['id']}, 'tmp_bill_id')}, 'pharmacy_fee')
        tmp_bill_laboratory_fee = state['TABLE_tmp_bill'].get({'tmp_bill_id': state['TABLE_tmp_bill'].get({'patient_id': argv['Op_Doctor_bill_run_8436']['id']}, 'tmp_bill_id')}, 'laboratory_fee')
        tmp_bill_appointment_fee = state['TABLE_tmp_bill'].get({'tmp_bill_id': state['TABLE_tmp_bill'].get({'patient_id': argv['Op_Doctor_bill_run_8436']['id']}, 'tmp_bill_id')}, 'appointment_fee')
        tmp_bill_vat = state['TABLE_tmp_bill'].get({'tmp_bill_id': state['TABLE_tmp_bill'].get({'patient_id': argv['Op_Doctor_bill_run_8436']['id']}, 'tmp_bill_id')}, 'vat')
        tmp_bill_discount = state['TABLE_tmp_bill'].get({'tmp_bill_id': state['TABLE_tmp_bill'].get({'patient_id': argv['Op_Doctor_bill_run_8436']['id']}, 'tmp_bill_id')}, 'discount')
        tmp_bill_consultant_id = state['TABLE_tmp_bill'].get({'tmp_bill_id': state['TABLE_tmp_bill'].get({'patient_id': argv['Op_Doctor_bill_run_8436']['id']}, 'tmp_bill_id')}, 'consultant_id')
        tmp_bill_patient_id = state['TABLE_tmp_bill'].get({'tmp_bill_id': state['TABLE_tmp_bill'].get({'patient_id': argv['Op_Doctor_bill_run_8436']['id']}, 'tmp_bill_id')}, 'patient_id')
        tmp_bill_laboratory_fee = 100
        state['TABLE_tmp_bill'].update({'tmp_bill_id': state['TABLE_tmp_bill'].get({'patient_id': argv['Op_Doctor_bill_run_8436']['id']}, 'tmp_bill_id')}, {'tmp_bill_id': tmp_bill_tmp_bill_id, 'doctor_fee': tmp_bill_doctor_fee, 'hospital_fee': tmp_bill_hospital_fee, 'pharmacy_fee': tmp_bill_pharmacy_fee, 'laboratory_fee': tmp_bill_laboratory_fee, 'appointment_fee': tmp_bill_appointment_fee, 'vat': tmp_bill_vat, 'discount': tmp_bill_discount, 'consultant_id': tmp_bill_consultant_id, 'patient_id': tmp_bill_patient_id})
        return state


class Op_LabAssistant_BloodGroupingTest_run_8437():
    def __init__(self):
        self.sops = [(self.cond0, self.csop0, self.sop0)]
        self.axiom = AxiomEmpty()

    def cond0(self, state, argv):
        newTstId = argv['Op_LabAssistant_BloodGroupingTest_run_8437']['newTstId']
        appId = argv['Op_LabAssistant_BloodGroupingTest_run_8437']['appId']
        bloodGroup = argv['Op_LabAssistant_BloodGroupingTest_run_8437']['bloodGroup']
        rh = argv['Op_LabAssistant_BloodGroupingTest_run_8437']['rh']
        now = argv['Op_LabAssistant_BloodGroupingTest_run_8437']['now']
        return (state['TABLE_BloodGroupingRh'].notNil({'tst_bloodG_id': argv['Op_LabAssistant_BloodGroupingTest_run_8437']['newTstId']}) == False)

    def csop0(self, state, argv):
        return True

    def sop0(self, state, argv):
        newTstId = argv['Op_LabAssistant_BloodGroupingTest_run_8437']['newTstId']
        appId = argv['Op_LabAssistant_BloodGroupingTest_run_8437']['appId']
        bloodGroup = argv['Op_LabAssistant_BloodGroupingTest_run_8437']['bloodGroup']
        rh = argv['Op_LabAssistant_BloodGroupingTest_run_8437']['rh']
        now = argv['Op_LabAssistant_BloodGroupingTest_run_8437']['now']
        BloodGroupingRh_tst_bloodG_id = argv['Op_LabAssistant_BloodGroupingTest_run_8437']['newTstId']
        BloodGroupingRh_appointment_id = argv['Op_LabAssistant_BloodGroupingTest_run_8437']['appId']
        BloodGroupingRh_bloodGroup = argv['Op_LabAssistant_BloodGroupingTest_run_8437']['bloodGroup']
        BloodGroupingRh_rhesusD = argv['Op_LabAssistant_BloodGroupingTest_run_8437']['rh']
        BloodGroupingRh_date = argv['Op_LabAssistant_BloodGroupingTest_run_8437']['now']
        state['TABLE_BloodGroupingRh'].add({'tst_bloodG_id': BloodGroupingRh_tst_bloodG_id}, {'appointment_id': BloodGroupingRh_appointment_id,'bloodGroup': BloodGroupingRh_bloodGroup,'rhesusD': BloodGroupingRh_rhesusD,'date': BloodGroupingRh_date})
        return state


class Op_Doctor_prescribe_run_8438():
    def __init__(self):
        self.sops = [(self.cond0, self.csop0, self.sop0)]
        self.axiom = AxiomEmpty()

    def cond0(self, state, argv):
        newPrescId = argv['Op_Doctor_prescribe_run_8438']['newPrescId']
        patientId = argv['Op_Doctor_prescribe_run_8438']['patientId']
        consultantId = argv['Op_Doctor_prescribe_run_8438']['consultantId']
        date = argv['Op_Doctor_prescribe_run_8438']['date']
        drugDose = argv['Op_Doctor_prescribe_run_8438']['drugDose']
        tests = argv['Op_Doctor_prescribe_run_8438']['tests']
        return (state['TABLE_prescription'].notNil({'prescription_id': argv['Op_Doctor_prescribe_run_8438']['newPrescId']}) == False)

    def csop0(self, state, argv):
        return True

    def sop0(self, state, argv):
        newPrescId = argv['Op_Doctor_prescribe_run_8438']['newPrescId']
        patientId = argv['Op_Doctor_prescribe_run_8438']['patientId']
        consultantId = argv['Op_Doctor_prescribe_run_8438']['consultantId']
        date = argv['Op_Doctor_prescribe_run_8438']['date']
        drugDose = argv['Op_Doctor_prescribe_run_8438']['drugDose']
        tests = argv['Op_Doctor_prescribe_run_8438']['tests']
        prescription_prescription_id = argv['Op_Doctor_prescribe_run_8438']['newPrescId']
        prescription_patient_id = argv['Op_Doctor_prescribe_run_8438']['patientId']
        prescription_consultant_id = argv['Op_Doctor_prescribe_run_8438']['consultantId']
        prescription_date = argv['Op_Doctor_prescribe_run_8438']['date']
        prescription_drugs_dose = argv['Op_Doctor_prescribe_run_8438']['drugDose']
        prescription_tests = argv['Op_Doctor_prescribe_run_8438']['tests']
        state['TABLE_prescription'].add({'prescription_id': prescription_prescription_id}, {'patient_id': prescription_patient_id,'consultant_id': prescription_consultant_id,'date': prescription_date,'drugs_dose': prescription_drugs_dose,'tests': prescription_tests})
        return state


class Op_Receptionist_setPatientInfo_run_8439():
    def __init__(self):
        self.sops = [(self.cond0, self.csop0, self.sop0), (self.cond1, self.csop1, self.sop1)]
        self.axiom = AxiomEmpty()

    def cond0(self, state, argv):
        newPersonId = argv['Op_Receptionist_setPatientInfo_run_8439']['newPersonId']
        newPatientId = argv['Op_Receptionist_setPatientInfo_run_8439']['newPatientId']
        nic = argv['Op_Receptionist_setPatientInfo_run_8439']['nic']
        gender = argv['Op_Receptionist_setPatientInfo_run_8439']['gender']
        birth = argv['Op_Receptionist_setPatientInfo_run_8439']['birth']
        address = argv['Op_Receptionist_setPatientInfo_run_8439']['address']
        mobile = argv['Op_Receptionist_setPatientInfo_run_8439']['mobile']
        firstName = argv['Op_Receptionist_setPatientInfo_run_8439']['firstName']
        lastName = argv['Op_Receptionist_setPatientInfo_run_8439']['lastName']
        email = argv['Op_Receptionist_setPatientInfo_run_8439']['email']
        nationality = argv['Op_Receptionist_setPatientInfo_run_8439']['nationality']
        religion = argv['Op_Receptionist_setPatientInfo_run_8439']['religion']
        newPersonId = argv['Op_Receptionist_setPatientInfo_run_8439']['newPersonId']
        newPatientId = argv['Op_Receptionist_setPatientInfo_run_8439']['newPatientId']
        nic = argv['Op_Receptionist_setPatientInfo_run_8439']['nic']
        gender = argv['Op_Receptionist_setPatientInfo_run_8439']['gender']
        birth = argv['Op_Receptionist_setPatientInfo_run_8439']['birth']
        address = argv['Op_Receptionist_setPatientInfo_run_8439']['address']
        mobile = argv['Op_Receptionist_setPatientInfo_run_8439']['mobile']
        firstName = argv['Op_Receptionist_setPatientInfo_run_8439']['firstName']
        lastName = argv['Op_Receptionist_setPatientInfo_run_8439']['lastName']
        email = argv['Op_Receptionist_setPatientInfo_run_8439']['email']
        nationality = argv['Op_Receptionist_setPatientInfo_run_8439']['nationality']
        religion = argv['Op_Receptionist_setPatientInfo_run_8439']['religion']
        patientInfo = argv['Op_Receptionist_setPatientInfo_run_8439']['patientInfo']
        return And((state['TABLE_person'].notNil({'person_id': argv['Op_Receptionist_setPatientInfo_run_8439']['newPersonId']}) == False),(state['TABLE_patient'].notNil({'patient_id': argv['Op_Receptionist_setPatientInfo_run_8439']['newPatientId']}) == False),Not((state['TABLE_person'].notNil({'person_id': argv['Op_Receptionist_setPatientInfo_run_8439']['newPersonId']}) == False)),Not((state['TABLE_patient'].notNil({'patient_id': argv['Op_Receptionist_setPatientInfo_run_8439']['newPatientId']}) == False)))

    def csop0(self, state, argv):
        return True

    def sop0(self, state, argv):
        newPersonId = argv['Op_Receptionist_setPatientInfo_run_8439']['newPersonId']
        newPatientId = argv['Op_Receptionist_setPatientInfo_run_8439']['newPatientId']
        nic = argv['Op_Receptionist_setPatientInfo_run_8439']['nic']
        gender = argv['Op_Receptionist_setPatientInfo_run_8439']['gender']
        birth = argv['Op_Receptionist_setPatientInfo_run_8439']['birth']
        address = argv['Op_Receptionist_setPatientInfo_run_8439']['address']
        mobile = argv['Op_Receptionist_setPatientInfo_run_8439']['mobile']
        firstName = argv['Op_Receptionist_setPatientInfo_run_8439']['firstName']
        lastName = argv['Op_Receptionist_setPatientInfo_run_8439']['lastName']
        email = argv['Op_Receptionist_setPatientInfo_run_8439']['email']
        nationality = argv['Op_Receptionist_setPatientInfo_run_8439']['nationality']
        religion = argv['Op_Receptionist_setPatientInfo_run_8439']['religion']
        person_person_id = argv['Op_Receptionist_setPatientInfo_run_8439']['newPersonId']
        person_user_id = StringVal('')
        person_nic = argv['Op_Receptionist_setPatientInfo_run_8439']['nic']
        person_gender = argv['Op_Receptionist_setPatientInfo_run_8439']['gender']
        person_date_of_birth = argv['Op_Receptionist_setPatientInfo_run_8439']['birth']
        person_address = argv['Op_Receptionist_setPatientInfo_run_8439']['address']
        person_mobile = argv['Op_Receptionist_setPatientInfo_run_8439']['mobile']
        person_first_name = argv['Op_Receptionist_setPatientInfo_run_8439']['firstName']
        person_last_name = argv['Op_Receptionist_setPatientInfo_run_8439']['lastName']
        person_email = argv['Op_Receptionist_setPatientInfo_run_8439']['email']
        person_nationality = argv['Op_Receptionist_setPatientInfo_run_8439']['nationality']
        person_religion = argv['Op_Receptionist_setPatientInfo_run_8439']['religion']
        state['TABLE_person'].add({'person_id': person_person_id}, {'user_id': person_user_id,'nic': person_nic,'gender': person_gender,'date_of_birth': person_date_of_birth,'address': person_address,'mobile': person_mobile,'first_name': person_first_name,'last_name': person_last_name,'email': person_email,'nationality': person_nationality,'religion': person_religion})
        return state

    def cond1(self, state, argv):
        newPersonId = argv['Op_Receptionist_setPatientInfo_run_8439']['newPersonId']
        newPatientId = argv['Op_Receptionist_setPatientInfo_run_8439']['newPatientId']
        nic = argv['Op_Receptionist_setPatientInfo_run_8439']['nic']
        gender = argv['Op_Receptionist_setPatientInfo_run_8439']['gender']
        birth = argv['Op_Receptionist_setPatientInfo_run_8439']['birth']
        address = argv['Op_Receptionist_setPatientInfo_run_8439']['address']
        mobile = argv['Op_Receptionist_setPatientInfo_run_8439']['mobile']
        firstName = argv['Op_Receptionist_setPatientInfo_run_8439']['firstName']
        lastName = argv['Op_Receptionist_setPatientInfo_run_8439']['lastName']
        email = argv['Op_Receptionist_setPatientInfo_run_8439']['email']
        nationality = argv['Op_Receptionist_setPatientInfo_run_8439']['nationality']
        religion = argv['Op_Receptionist_setPatientInfo_run_8439']['religion']
        patientInfo = argv['Op_Receptionist_setPatientInfo_run_8439']['patientInfo']
        return And((state['TABLE_person'].notNil({'person_id': argv['Op_Receptionist_setPatientInfo_run_8439']['newPersonId']}) == False),(state['TABLE_patient'].notNil({'patient_id': argv['Op_Receptionist_setPatientInfo_run_8439']['newPatientId']}) == False))

    def csop1(self, state, argv):
        return True

    def sop1(self, state, argv):
        newPersonId = argv['Op_Receptionist_setPatientInfo_run_8439']['newPersonId']
        newPatientId = argv['Op_Receptionist_setPatientInfo_run_8439']['newPatientId']
        nic = argv['Op_Receptionist_setPatientInfo_run_8439']['nic']
        gender = argv['Op_Receptionist_setPatientInfo_run_8439']['gender']
        birth = argv['Op_Receptionist_setPatientInfo_run_8439']['birth']
        address = argv['Op_Receptionist_setPatientInfo_run_8439']['address']
        mobile = argv['Op_Receptionist_setPatientInfo_run_8439']['mobile']
        firstName = argv['Op_Receptionist_setPatientInfo_run_8439']['firstName']
        lastName = argv['Op_Receptionist_setPatientInfo_run_8439']['lastName']
        email = argv['Op_Receptionist_setPatientInfo_run_8439']['email']
        nationality = argv['Op_Receptionist_setPatientInfo_run_8439']['nationality']
        religion = argv['Op_Receptionist_setPatientInfo_run_8439']['religion']
        patientInfo = argv['Op_Receptionist_setPatientInfo_run_8439']['patientInfo']
        person_person_id = argv['Op_Receptionist_setPatientInfo_run_8439']['newPersonId']
        person_user_id = StringVal('')
        person_nic = argv['Op_Receptionist_setPatientInfo_run_8439']['nic']
        person_gender = argv['Op_Receptionist_setPatientInfo_run_8439']['gender']
        person_date_of_birth = argv['Op_Receptionist_setPatientInfo_run_8439']['birth']
        person_address = argv['Op_Receptionist_setPatientInfo_run_8439']['address']
        person_mobile = argv['Op_Receptionist_setPatientInfo_run_8439']['mobile']
        person_first_name = argv['Op_Receptionist_setPatientInfo_run_8439']['firstName']
        person_last_name = argv['Op_Receptionist_setPatientInfo_run_8439']['lastName']
        person_email = argv['Op_Receptionist_setPatientInfo_run_8439']['email']
        person_nationality = argv['Op_Receptionist_setPatientInfo_run_8439']['nationality']
        person_religion = argv['Op_Receptionist_setPatientInfo_run_8439']['religion']
        state['TABLE_person'].add({'person_id': person_person_id}, {'user_id': person_user_id,'nic': person_nic,'gender': person_gender,'date_of_birth': person_date_of_birth,'address': person_address,'mobile': person_mobile,'first_name': person_first_name,'last_name': person_last_name,'email': person_email,'nationality': person_nationality,'religion': person_religion})
        patient_patient_id = argv['Op_Receptionist_setPatientInfo_run_8439']['newPatientId']
        patient_person_id = argv['Op_Receptionist_setPatientInfo_run_8439']['newPersonId']
        patient_drug_allergies_and_reactions = argv['Op_Receptionist_setPatientInfo_run_8439']['patientInfo']
        state['TABLE_patient'].add({'patient_id': patient_patient_id}, {'person_id': patient_person_id,'drug_allergies_and_reactions': patient_drug_allergies_and_reactions})
        return state


class Op_LabAssistant_RenalFunctionTest_run_8440():
    def __init__(self):
        self.sops = [(self.cond0, self.csop0, self.sop0)]
        self.axiom = AxiomEmpty()

    def cond0(self, state, argv):
        newTstId = argv['Op_LabAssistant_RenalFunctionTest_run_8440']['newTstId']
        appId = argv['Op_LabAssistant_RenalFunctionTest_run_8440']['appId']
        creatinine = argv['Op_LabAssistant_RenalFunctionTest_run_8440']['creatinine']
        urea = argv['Op_LabAssistant_RenalFunctionTest_run_8440']['urea']
        totalBilirubin = argv['Op_LabAssistant_RenalFunctionTest_run_8440']['totalBilirubin']
        directBilirubin = argv['Op_LabAssistant_RenalFunctionTest_run_8440']['directBilirubin']
        sgotast = argv['Op_LabAssistant_RenalFunctionTest_run_8440']['sgotast']
        sgptalt = argv['Op_LabAssistant_RenalFunctionTest_run_8440']['sgptalt']
        alkalinePhospates = argv['Op_LabAssistant_RenalFunctionTest_run_8440']['alkalinePhospates']
        now = argv['Op_LabAssistant_RenalFunctionTest_run_8440']['now']
        return (state['TABLE_RenalFunctionTest'].notNil({'tst_renal_id': argv['Op_LabAssistant_RenalFunctionTest_run_8440']['newTstId']}) == False)

    def csop0(self, state, argv):
        return True

    def sop0(self, state, argv):
        newTstId = argv['Op_LabAssistant_RenalFunctionTest_run_8440']['newTstId']
        appId = argv['Op_LabAssistant_RenalFunctionTest_run_8440']['appId']
        creatinine = argv['Op_LabAssistant_RenalFunctionTest_run_8440']['creatinine']
        urea = argv['Op_LabAssistant_RenalFunctionTest_run_8440']['urea']
        totalBilirubin = argv['Op_LabAssistant_RenalFunctionTest_run_8440']['totalBilirubin']
        directBilirubin = argv['Op_LabAssistant_RenalFunctionTest_run_8440']['directBilirubin']
        sgotast = argv['Op_LabAssistant_RenalFunctionTest_run_8440']['sgotast']
        sgptalt = argv['Op_LabAssistant_RenalFunctionTest_run_8440']['sgptalt']
        alkalinePhospates = argv['Op_LabAssistant_RenalFunctionTest_run_8440']['alkalinePhospates']
        now = argv['Op_LabAssistant_RenalFunctionTest_run_8440']['now']
        RenalFunctionTest_tst_renal_id = argv['Op_LabAssistant_RenalFunctionTest_run_8440']['newTstId']
        RenalFunctionTest_appointment_id = argv['Op_LabAssistant_RenalFunctionTest_run_8440']['appId']
        RenalFunctionTest_creatinine = argv['Op_LabAssistant_RenalFunctionTest_run_8440']['creatinine']
        RenalFunctionTest_urea = argv['Op_LabAssistant_RenalFunctionTest_run_8440']['urea']
        RenalFunctionTest_totalBilirubin = argv['Op_LabAssistant_RenalFunctionTest_run_8440']['totalBilirubin']
        RenalFunctionTest_directBilirubin = argv['Op_LabAssistant_RenalFunctionTest_run_8440']['directBilirubin']
        RenalFunctionTest_sgotast = argv['Op_LabAssistant_RenalFunctionTest_run_8440']['sgotast']
        RenalFunctionTest_sgptalt = argv['Op_LabAssistant_RenalFunctionTest_run_8440']['sgptalt']
        RenalFunctionTest_alkalinePhospates = argv['Op_LabAssistant_RenalFunctionTest_run_8440']['alkalinePhospates']
        RenalFunctionTest_date = argv['Op_LabAssistant_RenalFunctionTest_run_8440']['now']
        state['TABLE_RenalFunctionTest'].add({'tst_renal_id': RenalFunctionTest_tst_renal_id}, {'appointment_id': RenalFunctionTest_appointment_id,'creatinine': RenalFunctionTest_creatinine,'urea': RenalFunctionTest_urea,'totalBilirubin': RenalFunctionTest_totalBilirubin,'directBilirubin': RenalFunctionTest_directBilirubin,'sgotast': RenalFunctionTest_sgotast,'sgptalt': RenalFunctionTest_sgptalt,'alkalinePhospates': RenalFunctionTest_alkalinePhospates,'date': RenalFunctionTest_date})
        return state


class Op_Admin_updateProfileInfo_run_8441():
    def __init__(self):
        self.sops = [(self.cond0, self.csop0, self.sop0)]
        self.axiom = AxiomEmpty()

    def cond0(self, state, argv):
        id = argv['Op_Admin_updateProfileInfo_run_8441']['id']
        sys_user_person_id = argv['Op_Admin_updateProfileInfo_run_8441']['sys_user_person_id']
        person_person_id = argv['Op_Admin_updateProfileInfo_run_8441']['person_person_id']
        return And((state['TABLE_sys_user'].notNil({'user_id': argv['Op_Admin_updateProfileInfo_run_8441']['id']}) == True),(state['TABLE_person'].notNil({'person_id': state['TABLE_sys_user'].get({'user_id': argv['Op_Admin_updateProfileInfo_run_8441']['id']}, 'person_id')}) == True))

    def csop0(self, state, argv):
        return True

    def sop0(self, state, argv):
        id = argv['Op_Admin_updateProfileInfo_run_8441']['id']
        sys_user_person_id = argv['Op_Admin_updateProfileInfo_run_8441']['sys_user_person_id']
        person_person_id = argv['Op_Admin_updateProfileInfo_run_8441']['person_person_id']
        person_person_id = state['TABLE_person'].get({'person_id': state['TABLE_sys_user'].get({'user_id': argv['Op_Admin_updateProfileInfo_run_8441']['id']}, 'person_id')}, 'person_id')
        person_user_id = state['TABLE_person'].get({'person_id': state['TABLE_sys_user'].get({'user_id': argv['Op_Admin_updateProfileInfo_run_8441']['id']}, 'person_id')}, 'user_id')
        person_nic = state['TABLE_person'].get({'person_id': state['TABLE_sys_user'].get({'user_id': argv['Op_Admin_updateProfileInfo_run_8441']['id']}, 'person_id')}, 'nic')
        person_gender = state['TABLE_person'].get({'person_id': state['TABLE_sys_user'].get({'user_id': argv['Op_Admin_updateProfileInfo_run_8441']['id']}, 'person_id')}, 'gender')
        person_date_of_birth = state['TABLE_person'].get({'person_id': state['TABLE_sys_user'].get({'user_id': argv['Op_Admin_updateProfileInfo_run_8441']['id']}, 'person_id')}, 'date_of_birth')
        person_address = state['TABLE_person'].get({'person_id': state['TABLE_sys_user'].get({'user_id': argv['Op_Admin_updateProfileInfo_run_8441']['id']}, 'person_id')}, 'address')
        person_mobile = state['TABLE_person'].get({'person_id': state['TABLE_sys_user'].get({'user_id': argv['Op_Admin_updateProfileInfo_run_8441']['id']}, 'person_id')}, 'mobile')
        person_first_name = state['TABLE_person'].get({'person_id': state['TABLE_sys_user'].get({'user_id': argv['Op_Admin_updateProfileInfo_run_8441']['id']}, 'person_id')}, 'first_name')
        person_last_name = state['TABLE_person'].get({'person_id': state['TABLE_sys_user'].get({'user_id': argv['Op_Admin_updateProfileInfo_run_8441']['id']}, 'person_id')}, 'last_name')
        person_email = state['TABLE_person'].get({'person_id': state['TABLE_sys_user'].get({'user_id': argv['Op_Admin_updateProfileInfo_run_8441']['id']}, 'person_id')}, 'email')
        person_nationality = state['TABLE_person'].get({'person_id': state['TABLE_sys_user'].get({'user_id': argv['Op_Admin_updateProfileInfo_run_8441']['id']}, 'person_id')}, 'nationality')
        person_religion = state['TABLE_person'].get({'person_id': state['TABLE_sys_user'].get({'user_id': argv['Op_Admin_updateProfileInfo_run_8441']['id']}, 'person_id')}, 'religion')
        person_address = argv['Op_Admin_updateProfileInfo_run_8441']['id']
        state['TABLE_person'].update({'person_id': state['TABLE_sys_user'].get({'user_id': argv['Op_Admin_updateProfileInfo_run_8441']['id']}, 'person_id')}, {'person_id': person_person_id, 'user_id': person_user_id, 'nic': person_nic, 'gender': person_gender, 'date_of_birth': person_date_of_birth, 'address': person_address, 'mobile': person_mobile, 'first_name': person_first_name, 'last_name': person_last_name, 'email': person_email, 'nationality': person_nationality, 'religion': person_religion})
        return state


class Op_Admin_resetPassword_run_8442():
    def __init__(self):
        self.sops = [(self.cond0, self.csop0, self.sop0)]
        self.axiom = AxiomEmpty()

    def cond0(self, state, argv):
        id = argv['Op_Admin_resetPassword_run_8442']['id']
        sys_user_user_id = argv['Op_Admin_resetPassword_run_8442']['sys_user_user_id']
        return (state['TABLE_sys_user'].notNil({'user_id': argv['Op_Admin_resetPassword_run_8442']['id']}) == True)

    def csop0(self, state, argv):
        return True

    def sop0(self, state, argv):
        id = argv['Op_Admin_resetPassword_run_8442']['id']
        sys_user_user_id = argv['Op_Admin_resetPassword_run_8442']['sys_user_user_id']
        sys_user_person_id = state['TABLE_sys_user'].get({'user_id': argv['Op_Admin_resetPassword_run_8442']['id']}, 'person_id')
        sys_user_user_id = state['TABLE_sys_user'].get({'user_id': argv['Op_Admin_resetPassword_run_8442']['id']}, 'user_id')
        sys_user_user_name = state['TABLE_sys_user'].get({'user_id': argv['Op_Admin_resetPassword_run_8442']['id']}, 'user_name')
        sys_user_user_type = state['TABLE_sys_user'].get({'user_id': argv['Op_Admin_resetPassword_run_8442']['id']}, 'user_type')
        sys_user_other_info = state['TABLE_sys_user'].get({'user_id': argv['Op_Admin_resetPassword_run_8442']['id']}, 'other_info')
        sys_user_password = state['TABLE_sys_user'].get({'user_id': argv['Op_Admin_resetPassword_run_8442']['id']}, 'password')
        sys_user_online = state['TABLE_sys_user'].get({'user_id': argv['Op_Admin_resetPassword_run_8442']['id']}, 'online')
        sys_user_login = state['TABLE_sys_user'].get({'user_id': argv['Op_Admin_resetPassword_run_8442']['id']}, 'login')
        sys_user_logout = state['TABLE_sys_user'].get({'user_id': argv['Op_Admin_resetPassword_run_8442']['id']}, 'logout')
        sys_user_profile_pic = state['TABLE_sys_user'].get({'user_id': argv['Op_Admin_resetPassword_run_8442']['id']}, 'profile_pic')
        sys_user_suspend = state['TABLE_sys_user'].get({'user_id': argv['Op_Admin_resetPassword_run_8442']['id']}, 'suspend')
        sys_user_password = StringVal('123456')
        state['TABLE_sys_user'].update({'user_id': argv['Op_Admin_resetPassword_run_8442']['id']}, {'person_id': sys_user_person_id, 'user_id': sys_user_user_id, 'user_name': sys_user_user_name, 'user_type': sys_user_user_type, 'other_info': sys_user_other_info, 'password': sys_user_password, 'online': sys_user_online, 'login': sys_user_login, 'logout': sys_user_logout, 'profile_pic': sys_user_profile_pic, 'suspend': sys_user_suspend})
        return state


class Op_Receptionist_refund_run_8443():
    def __init__(self):
        self.sops = [(self.cond0, self.csop0, self.sop0)]
        self.axiom = AxiomEmpty()

    def cond0(self, state, argv):
        newRefundId = argv['Op_Receptionist_refund_run_8443']['newRefundId']
        billId = argv['Op_Receptionist_refund_run_8443']['billId']
        paymentType = argv['Op_Receptionist_refund_run_8443']['paymentType']
        reason = argv['Op_Receptionist_refund_run_8443']['reason']
        amount = argv['Op_Receptionist_refund_run_8443']['amount']
        now = argv['Op_Receptionist_refund_run_8443']['now']
        return (state['TABLE_refund'].notNil({'refund_id': argv['Op_Receptionist_refund_run_8443']['newRefundId']}) == False)

    def csop0(self, state, argv):
        return True

    def sop0(self, state, argv):
        newRefundId = argv['Op_Receptionist_refund_run_8443']['newRefundId']
        billId = argv['Op_Receptionist_refund_run_8443']['billId']
        paymentType = argv['Op_Receptionist_refund_run_8443']['paymentType']
        reason = argv['Op_Receptionist_refund_run_8443']['reason']
        amount = argv['Op_Receptionist_refund_run_8443']['amount']
        now = argv['Op_Receptionist_refund_run_8443']['now']
        refund_refund_id = argv['Op_Receptionist_refund_run_8443']['newRefundId']
        refund_bill_id = argv['Op_Receptionist_refund_run_8443']['billId']
        refund_payment_type = argv['Op_Receptionist_refund_run_8443']['paymentType']
        refund_reason = argv['Op_Receptionist_refund_run_8443']['reason']
        refund_amount = argv['Op_Receptionist_refund_run_8443']['amount']
        refund_date = argv['Op_Receptionist_refund_run_8443']['now']
        state['TABLE_refund'].add({'refund_id': refund_refund_id}, {'bill_id': refund_bill_id,'payment_type': refund_payment_type,'reason': refund_reason,'amount': refund_amount,'date': refund_date})
        return state


class Op_Admin_unsuspendUser_run_8444():
    def __init__(self):
        self.sops = [(self.cond0, self.csop0, self.sop0)]
        self.axiom = AxiomEmpty()

    def cond0(self, state, argv):
        id = argv['Op_Admin_unsuspendUser_run_8444']['id']
        sys_user_user_id = argv['Op_Admin_unsuspendUser_run_8444']['sys_user_user_id']
        return (state['TABLE_sys_user'].notNil({'user_id': argv['Op_Admin_unsuspendUser_run_8444']['id']}) == True)

    def csop0(self, state, argv):
        return True

    def sop0(self, state, argv):
        id = argv['Op_Admin_unsuspendUser_run_8444']['id']
        sys_user_user_id = argv['Op_Admin_unsuspendUser_run_8444']['sys_user_user_id']
        sys_user_person_id = state['TABLE_sys_user'].get({'user_id': argv['Op_Admin_unsuspendUser_run_8444']['id']}, 'person_id')
        sys_user_user_id = state['TABLE_sys_user'].get({'user_id': argv['Op_Admin_unsuspendUser_run_8444']['id']}, 'user_id')
        sys_user_user_name = state['TABLE_sys_user'].get({'user_id': argv['Op_Admin_unsuspendUser_run_8444']['id']}, 'user_name')
        sys_user_user_type = state['TABLE_sys_user'].get({'user_id': argv['Op_Admin_unsuspendUser_run_8444']['id']}, 'user_type')
        sys_user_other_info = state['TABLE_sys_user'].get({'user_id': argv['Op_Admin_unsuspendUser_run_8444']['id']}, 'other_info')
        sys_user_password = state['TABLE_sys_user'].get({'user_id': argv['Op_Admin_unsuspendUser_run_8444']['id']}, 'password')
        sys_user_online = state['TABLE_sys_user'].get({'user_id': argv['Op_Admin_unsuspendUser_run_8444']['id']}, 'online')
        sys_user_login = state['TABLE_sys_user'].get({'user_id': argv['Op_Admin_unsuspendUser_run_8444']['id']}, 'login')
        sys_user_logout = state['TABLE_sys_user'].get({'user_id': argv['Op_Admin_unsuspendUser_run_8444']['id']}, 'logout')
        sys_user_profile_pic = state['TABLE_sys_user'].get({'user_id': argv['Op_Admin_unsuspendUser_run_8444']['id']}, 'profile_pic')
        sys_user_suspend = state['TABLE_sys_user'].get({'user_id': argv['Op_Admin_unsuspendUser_run_8444']['id']}, 'suspend')
        sys_user_suspend = 0
        state['TABLE_sys_user'].update({'user_id': argv['Op_Admin_unsuspendUser_run_8444']['id']}, {'person_id': sys_user_person_id, 'user_id': sys_user_user_id, 'user_name': sys_user_user_name, 'user_type': sys_user_user_type, 'other_info': sys_user_other_info, 'password': sys_user_password, 'online': sys_user_online, 'login': sys_user_login, 'logout': sys_user_logout, 'profile_pic': sys_user_profile_pic, 'suspend': sys_user_suspend})
        return state


class Op_Receptionist_makeLabAppointment_run_8445():
    def __init__(self):
        self.sops = [(self.cond0, self.csop0, self.sop0), (self.cond1, self.csop1, self.sop1), (self.cond2, self.csop2, self.sop2)]
        self.axiom = AxiomEmpty()

    def cond0(self, state, argv):
        newAppId = argv['Op_Receptionist_makeLabAppointment_run_8445']['newAppId']
        testId = argv['Op_Receptionist_makeLabAppointment_run_8445']['testId']
        patientId = argv['Op_Receptionist_makeLabAppointment_run_8445']['patientId']
        doctorId = argv['Op_Receptionist_makeLabAppointment_run_8445']['doctorId']
        currentDate = argv['Op_Receptionist_makeLabAppointment_run_8445']['currentDate']
        day = argv['Op_Receptionist_makeLabAppointment_run_8445']['day']
        newAppId = argv['Op_Receptionist_makeLabAppointment_run_8445']['newAppId']
        testId = argv['Op_Receptionist_makeLabAppointment_run_8445']['testId']
        patientId = argv['Op_Receptionist_makeLabAppointment_run_8445']['patientId']
        doctorId = argv['Op_Receptionist_makeLabAppointment_run_8445']['doctorId']
        currentDate = argv['Op_Receptionist_makeLabAppointment_run_8445']['currentDate']
        day = argv['Op_Receptionist_makeLabAppointment_run_8445']['day']
        lab_test_test_fee = argv['Op_Receptionist_makeLabAppointment_run_8445']['lab_test_test_fee']
        tmp_bill_tmp_bill_id = argv['Op_Receptionist_makeLabAppointment_run_8445']['tmp_bill_tmp_bill_id']
        newAppId = argv['Op_Receptionist_makeLabAppointment_run_8445']['newAppId']
        testId = argv['Op_Receptionist_makeLabAppointment_run_8445']['testId']
        patientId = argv['Op_Receptionist_makeLabAppointment_run_8445']['patientId']
        doctorId = argv['Op_Receptionist_makeLabAppointment_run_8445']['doctorId']
        currentDate = argv['Op_Receptionist_makeLabAppointment_run_8445']['currentDate']
        day = argv['Op_Receptionist_makeLabAppointment_run_8445']['day']
        lab_test_test_fee = argv['Op_Receptionist_makeLabAppointment_run_8445']['lab_test_test_fee']
        newTmpBillId = argv['Op_Receptionist_makeLabAppointment_run_8445']['newTmpBillId']
        return And((state['TABLE_lab_appointment'].notNil({'lab_appointment_id': argv['Op_Receptionist_makeLabAppointment_run_8445']['newAppId']}) == False),Not((state['TABLE_lab_appointment'].notNil({'lab_appointment_id': argv['Op_Receptionist_makeLabAppointment_run_8445']['newAppId']}) == False)),Not((state['TABLE_lab_test'].notNil({'test_id': argv['Op_Receptionist_makeLabAppointment_run_8445']['testId']}) == True)),Not((state['TABLE_tmp_bill'].notNil({'patient_id': argv['Op_Receptionist_makeLabAppointment_run_8445']['patientId']}) == True)),Not((state['TABLE_tmp_bill'].notNil({'tmp_bill_id': state['TABLE_tmp_bill'].get({'patient_id': argv['Op_Receptionist_makeLabAppointment_run_8445']['patientId']}, 'tmp_bill_id')}) == True)),Not((state['TABLE_lab_appointment'].notNil({'lab_appointment_id': argv['Op_Receptionist_makeLabAppointment_run_8445']['newAppId']}) == False)),Not((state['TABLE_lab_test'].notNil({'test_id': argv['Op_Receptionist_makeLabAppointment_run_8445']['testId']}) == True)),Not((state['TABLE_tmp_bill'].notNil({'patient_id': argv['Op_Receptionist_makeLabAppointment_run_8445']['patientId']}) == False)))

    def csop0(self, state, argv):
        return True

    def sop0(self, state, argv):
        newAppId = argv['Op_Receptionist_makeLabAppointment_run_8445']['newAppId']
        testId = argv['Op_Receptionist_makeLabAppointment_run_8445']['testId']
        patientId = argv['Op_Receptionist_makeLabAppointment_run_8445']['patientId']
        doctorId = argv['Op_Receptionist_makeLabAppointment_run_8445']['doctorId']
        currentDate = argv['Op_Receptionist_makeLabAppointment_run_8445']['currentDate']
        day = argv['Op_Receptionist_makeLabAppointment_run_8445']['day']
        lab_appointment_lab_appointment_id = argv['Op_Receptionist_makeLabAppointment_run_8445']['newAppId']
        lab_appointment_test_id = argv['Op_Receptionist_makeLabAppointment_run_8445']['testId']
        lab_appointment_patient_id = argv['Op_Receptionist_makeLabAppointment_run_8445']['patientId']
        lab_appointment_doctor_id = argv['Op_Receptionist_makeLabAppointment_run_8445']['doctorId']
        lab_appointment_date = (argv['Op_Receptionist_makeLabAppointment_run_8445']['currentDate'])+(argv['Op_Receptionist_makeLabAppointment_run_8445']['day'])
        lab_appointment_cancelled = False
        state['TABLE_lab_appointment'].add({'lab_appointment_id': lab_appointment_lab_appointment_id}, {'test_id': lab_appointment_test_id,'patient_id': lab_appointment_patient_id,'doctor_id': lab_appointment_doctor_id,'date': lab_appointment_date,'cancelled': lab_appointment_cancelled})
        return state

    def cond1(self, state, argv):
        newAppId = argv['Op_Receptionist_makeLabAppointment_run_8445']['newAppId']
        testId = argv['Op_Receptionist_makeLabAppointment_run_8445']['testId']
        patientId = argv['Op_Receptionist_makeLabAppointment_run_8445']['patientId']
        doctorId = argv['Op_Receptionist_makeLabAppointment_run_8445']['doctorId']
        currentDate = argv['Op_Receptionist_makeLabAppointment_run_8445']['currentDate']
        day = argv['Op_Receptionist_makeLabAppointment_run_8445']['day']
        lab_test_test_fee = argv['Op_Receptionist_makeLabAppointment_run_8445']['lab_test_test_fee']
        tmp_bill_tmp_bill_id = argv['Op_Receptionist_makeLabAppointment_run_8445']['tmp_bill_tmp_bill_id']
        return And((state['TABLE_lab_appointment'].notNil({'lab_appointment_id': argv['Op_Receptionist_makeLabAppointment_run_8445']['newAppId']}) == False),(state['TABLE_lab_test'].notNil({'test_id': argv['Op_Receptionist_makeLabAppointment_run_8445']['testId']}) == True),(state['TABLE_tmp_bill'].notNil({'patient_id': argv['Op_Receptionist_makeLabAppointment_run_8445']['patientId']}) == True),(state['TABLE_tmp_bill'].notNil({'tmp_bill_id': state['TABLE_tmp_bill'].get({'patient_id': argv['Op_Receptionist_makeLabAppointment_run_8445']['patientId']}, 'tmp_bill_id')}) == True))

    def csop1(self, state, argv):
        return True

    def sop1(self, state, argv):
        newAppId = argv['Op_Receptionist_makeLabAppointment_run_8445']['newAppId']
        testId = argv['Op_Receptionist_makeLabAppointment_run_8445']['testId']
        patientId = argv['Op_Receptionist_makeLabAppointment_run_8445']['patientId']
        doctorId = argv['Op_Receptionist_makeLabAppointment_run_8445']['doctorId']
        currentDate = argv['Op_Receptionist_makeLabAppointment_run_8445']['currentDate']
        day = argv['Op_Receptionist_makeLabAppointment_run_8445']['day']
        lab_test_test_fee = argv['Op_Receptionist_makeLabAppointment_run_8445']['lab_test_test_fee']
        tmp_bill_tmp_bill_id = argv['Op_Receptionist_makeLabAppointment_run_8445']['tmp_bill_tmp_bill_id']
        lab_appointment_lab_appointment_id = argv['Op_Receptionist_makeLabAppointment_run_8445']['newAppId']
        lab_appointment_test_id = argv['Op_Receptionist_makeLabAppointment_run_8445']['testId']
        lab_appointment_patient_id = argv['Op_Receptionist_makeLabAppointment_run_8445']['patientId']
        lab_appointment_doctor_id = argv['Op_Receptionist_makeLabAppointment_run_8445']['doctorId']
        lab_appointment_date = (argv['Op_Receptionist_makeLabAppointment_run_8445']['currentDate'])+(argv['Op_Receptionist_makeLabAppointment_run_8445']['day'])
        lab_appointment_cancelled = False
        state['TABLE_lab_appointment'].add({'lab_appointment_id': lab_appointment_lab_appointment_id}, {'test_id': lab_appointment_test_id,'patient_id': lab_appointment_patient_id,'doctor_id': lab_appointment_doctor_id,'date': lab_appointment_date,'cancelled': lab_appointment_cancelled})
        tmp_bill_tmp_bill_id = state['TABLE_tmp_bill'].get({'tmp_bill_id': state['TABLE_tmp_bill'].get({'patient_id': argv['Op_Receptionist_makeLabAppointment_run_8445']['patientId']}, 'tmp_bill_id')}, 'tmp_bill_id')
        tmp_bill_doctor_fee = state['TABLE_tmp_bill'].get({'tmp_bill_id': state['TABLE_tmp_bill'].get({'patient_id': argv['Op_Receptionist_makeLabAppointment_run_8445']['patientId']}, 'tmp_bill_id')}, 'doctor_fee')
        tmp_bill_hospital_fee = state['TABLE_tmp_bill'].get({'tmp_bill_id': state['TABLE_tmp_bill'].get({'patient_id': argv['Op_Receptionist_makeLabAppointment_run_8445']['patientId']}, 'tmp_bill_id')}, 'hospital_fee')
        tmp_bill_pharmacy_fee = state['TABLE_tmp_bill'].get({'tmp_bill_id': state['TABLE_tmp_bill'].get({'patient_id': argv['Op_Receptionist_makeLabAppointment_run_8445']['patientId']}, 'tmp_bill_id')}, 'pharmacy_fee')
        tmp_bill_laboratory_fee = state['TABLE_tmp_bill'].get({'tmp_bill_id': state['TABLE_tmp_bill'].get({'patient_id': argv['Op_Receptionist_makeLabAppointment_run_8445']['patientId']}, 'tmp_bill_id')}, 'laboratory_fee')
        tmp_bill_appointment_fee = state['TABLE_tmp_bill'].get({'tmp_bill_id': state['TABLE_tmp_bill'].get({'patient_id': argv['Op_Receptionist_makeLabAppointment_run_8445']['patientId']}, 'tmp_bill_id')}, 'appointment_fee')
        tmp_bill_vat = state['TABLE_tmp_bill'].get({'tmp_bill_id': state['TABLE_tmp_bill'].get({'patient_id': argv['Op_Receptionist_makeLabAppointment_run_8445']['patientId']}, 'tmp_bill_id')}, 'vat')
        tmp_bill_discount = state['TABLE_tmp_bill'].get({'tmp_bill_id': state['TABLE_tmp_bill'].get({'patient_id': argv['Op_Receptionist_makeLabAppointment_run_8445']['patientId']}, 'tmp_bill_id')}, 'discount')
        tmp_bill_consultant_id = state['TABLE_tmp_bill'].get({'tmp_bill_id': state['TABLE_tmp_bill'].get({'patient_id': argv['Op_Receptionist_makeLabAppointment_run_8445']['patientId']}, 'tmp_bill_id')}, 'consultant_id')
        tmp_bill_patient_id = state['TABLE_tmp_bill'].get({'tmp_bill_id': state['TABLE_tmp_bill'].get({'patient_id': argv['Op_Receptionist_makeLabAppointment_run_8445']['patientId']}, 'tmp_bill_id')}, 'patient_id')
        tmp_bill_laboratory_fee = state['TABLE_lab_test'].get({'test_id': argv['Op_Receptionist_makeLabAppointment_run_8445']['testId']}, 'test_fee')
        state['TABLE_tmp_bill'].update({'tmp_bill_id': state['TABLE_tmp_bill'].get({'patient_id': argv['Op_Receptionist_makeLabAppointment_run_8445']['patientId']}, 'tmp_bill_id')}, {'tmp_bill_id': tmp_bill_tmp_bill_id, 'doctor_fee': tmp_bill_doctor_fee, 'hospital_fee': tmp_bill_hospital_fee, 'pharmacy_fee': tmp_bill_pharmacy_fee, 'laboratory_fee': tmp_bill_laboratory_fee, 'appointment_fee': tmp_bill_appointment_fee, 'vat': tmp_bill_vat, 'discount': tmp_bill_discount, 'consultant_id': tmp_bill_consultant_id, 'patient_id': tmp_bill_patient_id})
        return state

    def cond2(self, state, argv):
        newAppId = argv['Op_Receptionist_makeLabAppointment_run_8445']['newAppId']
        testId = argv['Op_Receptionist_makeLabAppointment_run_8445']['testId']
        patientId = argv['Op_Receptionist_makeLabAppointment_run_8445']['patientId']
        doctorId = argv['Op_Receptionist_makeLabAppointment_run_8445']['doctorId']
        currentDate = argv['Op_Receptionist_makeLabAppointment_run_8445']['currentDate']
        day = argv['Op_Receptionist_makeLabAppointment_run_8445']['day']
        lab_test_test_fee = argv['Op_Receptionist_makeLabAppointment_run_8445']['lab_test_test_fee']
        newTmpBillId = argv['Op_Receptionist_makeLabAppointment_run_8445']['newTmpBillId']
        return And((state['TABLE_lab_appointment'].notNil({'lab_appointment_id': argv['Op_Receptionist_makeLabAppointment_run_8445']['newAppId']}) == False),(state['TABLE_lab_test'].notNil({'test_id': argv['Op_Receptionist_makeLabAppointment_run_8445']['testId']}) == True),(state['TABLE_tmp_bill'].notNil({'patient_id': argv['Op_Receptionist_makeLabAppointment_run_8445']['patientId']}) == False))

    def csop2(self, state, argv):
        return True

    def sop2(self, state, argv):
        newAppId = argv['Op_Receptionist_makeLabAppointment_run_8445']['newAppId']
        testId = argv['Op_Receptionist_makeLabAppointment_run_8445']['testId']
        patientId = argv['Op_Receptionist_makeLabAppointment_run_8445']['patientId']
        doctorId = argv['Op_Receptionist_makeLabAppointment_run_8445']['doctorId']
        currentDate = argv['Op_Receptionist_makeLabAppointment_run_8445']['currentDate']
        day = argv['Op_Receptionist_makeLabAppointment_run_8445']['day']
        lab_test_test_fee = argv['Op_Receptionist_makeLabAppointment_run_8445']['lab_test_test_fee']
        newTmpBillId = argv['Op_Receptionist_makeLabAppointment_run_8445']['newTmpBillId']
        lab_appointment_lab_appointment_id = argv['Op_Receptionist_makeLabAppointment_run_8445']['newAppId']
        lab_appointment_test_id = argv['Op_Receptionist_makeLabAppointment_run_8445']['testId']
        lab_appointment_patient_id = argv['Op_Receptionist_makeLabAppointment_run_8445']['patientId']
        lab_appointment_doctor_id = argv['Op_Receptionist_makeLabAppointment_run_8445']['doctorId']
        lab_appointment_date = (argv['Op_Receptionist_makeLabAppointment_run_8445']['currentDate'])+(argv['Op_Receptionist_makeLabAppointment_run_8445']['day'])
        lab_appointment_cancelled = False
        state['TABLE_lab_appointment'].add({'lab_appointment_id': lab_appointment_lab_appointment_id}, {'test_id': lab_appointment_test_id,'patient_id': lab_appointment_patient_id,'doctor_id': lab_appointment_doctor_id,'date': lab_appointment_date,'cancelled': lab_appointment_cancelled})
        tmp_bill_tmp_bill_id = argv['Op_Receptionist_makeLabAppointment_run_8445']['newTmpBillId']
        tmp_bill_patient_id = argv['Op_Receptionist_makeLabAppointment_run_8445']['patientId']
        tmp_bill_laboratory_fee = state['TABLE_lab_test'].get({'test_id': argv['Op_Receptionist_makeLabAppointment_run_8445']['testId']}, 'test_fee')
        state['TABLE_tmp_bill'].add({'tmp_bill_id': tmp_bill_tmp_bill_id}, {'patient_id': tmp_bill_patient_id,'laboratory_fee': tmp_bill_laboratory_fee})
        return state


class Op_LabAssistant_LipidTest_run_8446():
    def __init__(self):
        self.sops = [(self.cond0, self.csop0, self.sop0)]
        self.axiom = AxiomEmpty()

    def cond0(self, state, argv):
        newTstId = argv['Op_LabAssistant_LipidTest_run_8446']['newTstId']
        appId = argv['Op_LabAssistant_LipidTest_run_8446']['appId']
        cholestrolHDL = argv['Op_LabAssistant_LipidTest_run_8446']['cholestrolHDL']
        cholestrolLDL = argv['Op_LabAssistant_LipidTest_run_8446']['cholestrolLDL']
        triglycerides = argv['Op_LabAssistant_LipidTest_run_8446']['triglycerides']
        totalCholestrolLDLHDLratio = argv['Op_LabAssistant_LipidTest_run_8446']['totalCholestrolLDLHDLratio']
        now = argv['Op_LabAssistant_LipidTest_run_8446']['now']
        return (state['TABLE_LipidTest'].notNil({'tst_li_id': argv['Op_LabAssistant_LipidTest_run_8446']['newTstId']}) == False)

    def csop0(self, state, argv):
        return True

    def sop0(self, state, argv):
        newTstId = argv['Op_LabAssistant_LipidTest_run_8446']['newTstId']
        appId = argv['Op_LabAssistant_LipidTest_run_8446']['appId']
        cholestrolHDL = argv['Op_LabAssistant_LipidTest_run_8446']['cholestrolHDL']
        cholestrolLDL = argv['Op_LabAssistant_LipidTest_run_8446']['cholestrolLDL']
        triglycerides = argv['Op_LabAssistant_LipidTest_run_8446']['triglycerides']
        totalCholestrolLDLHDLratio = argv['Op_LabAssistant_LipidTest_run_8446']['totalCholestrolLDLHDLratio']
        now = argv['Op_LabAssistant_LipidTest_run_8446']['now']
        LipidTest_tst_li_id = argv['Op_LabAssistant_LipidTest_run_8446']['newTstId']
        LipidTest_appointment_id = argv['Op_LabAssistant_LipidTest_run_8446']['appId']
        LipidTest_cholestrolHDL = argv['Op_LabAssistant_LipidTest_run_8446']['cholestrolHDL']
        LipidTest_cholestrolLDL = argv['Op_LabAssistant_LipidTest_run_8446']['cholestrolLDL']
        LipidTest_triglycerides = argv['Op_LabAssistant_LipidTest_run_8446']['triglycerides']
        LipidTest_totalCholestrolLDLHDLratio = argv['Op_LabAssistant_LipidTest_run_8446']['totalCholestrolLDLHDLratio']
        LipidTest_date = argv['Op_LabAssistant_LipidTest_run_8446']['now']
        state['TABLE_LipidTest'].add({'tst_li_id': LipidTest_tst_li_id}, {'appointment_id': LipidTest_appointment_id,'cholestrolHDL': LipidTest_cholestrolHDL,'cholestrolLDL': LipidTest_cholestrolLDL,'triglycerides': LipidTest_triglycerides,'totalCholestrolLDLHDLratio': LipidTest_totalCholestrolLDLHDLratio,'date': LipidTest_date})
        return state


class Op_Doctor_updateAccountInfo_run_8447():
    def __init__(self):
        self.sops = [(self.cond0, self.csop0, self.sop0)]
        self.axiom = AxiomEmpty()

    def cond0(self, state, argv):
        id = argv['Op_Doctor_updateAccountInfo_run_8447']['id']
        doctor_user_id = argv['Op_Doctor_updateAccountInfo_run_8447']['doctor_user_id']
        sys_user_user_id = argv['Op_Doctor_updateAccountInfo_run_8447']['sys_user_user_id']
        return And((state['TABLE_doctor'].notNil({'slmc_reg_no': argv['Op_Doctor_updateAccountInfo_run_8447']['id']}) == True),(state['TABLE_sys_user'].notNil({'user_id': state['TABLE_doctor'].get({'slmc_reg_no': argv['Op_Doctor_updateAccountInfo_run_8447']['id']}, 'user_id')}) == True))

    def csop0(self, state, argv):
        return True

    def sop0(self, state, argv):
        id = argv['Op_Doctor_updateAccountInfo_run_8447']['id']
        doctor_user_id = argv['Op_Doctor_updateAccountInfo_run_8447']['doctor_user_id']
        sys_user_user_id = argv['Op_Doctor_updateAccountInfo_run_8447']['sys_user_user_id']
        sys_user_person_id = state['TABLE_sys_user'].get({'user_id': state['TABLE_doctor'].get({'slmc_reg_no': argv['Op_Doctor_updateAccountInfo_run_8447']['id']}, 'user_id')}, 'person_id')
        sys_user_user_id = state['TABLE_sys_user'].get({'user_id': state['TABLE_doctor'].get({'slmc_reg_no': argv['Op_Doctor_updateAccountInfo_run_8447']['id']}, 'user_id')}, 'user_id')
        sys_user_user_name = state['TABLE_sys_user'].get({'user_id': state['TABLE_doctor'].get({'slmc_reg_no': argv['Op_Doctor_updateAccountInfo_run_8447']['id']}, 'user_id')}, 'user_name')
        sys_user_user_type = state['TABLE_sys_user'].get({'user_id': state['TABLE_doctor'].get({'slmc_reg_no': argv['Op_Doctor_updateAccountInfo_run_8447']['id']}, 'user_id')}, 'user_type')
        sys_user_other_info = state['TABLE_sys_user'].get({'user_id': state['TABLE_doctor'].get({'slmc_reg_no': argv['Op_Doctor_updateAccountInfo_run_8447']['id']}, 'user_id')}, 'other_info')
        sys_user_password = state['TABLE_sys_user'].get({'user_id': state['TABLE_doctor'].get({'slmc_reg_no': argv['Op_Doctor_updateAccountInfo_run_8447']['id']}, 'user_id')}, 'password')
        sys_user_online = state['TABLE_sys_user'].get({'user_id': state['TABLE_doctor'].get({'slmc_reg_no': argv['Op_Doctor_updateAccountInfo_run_8447']['id']}, 'user_id')}, 'online')
        sys_user_login = state['TABLE_sys_user'].get({'user_id': state['TABLE_doctor'].get({'slmc_reg_no': argv['Op_Doctor_updateAccountInfo_run_8447']['id']}, 'user_id')}, 'login')
        sys_user_logout = state['TABLE_sys_user'].get({'user_id': state['TABLE_doctor'].get({'slmc_reg_no': argv['Op_Doctor_updateAccountInfo_run_8447']['id']}, 'user_id')}, 'logout')
        sys_user_profile_pic = state['TABLE_sys_user'].get({'user_id': state['TABLE_doctor'].get({'slmc_reg_no': argv['Op_Doctor_updateAccountInfo_run_8447']['id']}, 'user_id')}, 'profile_pic')
        sys_user_suspend = state['TABLE_sys_user'].get({'user_id': state['TABLE_doctor'].get({'slmc_reg_no': argv['Op_Doctor_updateAccountInfo_run_8447']['id']}, 'user_id')}, 'suspend')
        sys_user_other_info = argv['Op_Doctor_updateAccountInfo_run_8447']['id']
        state['TABLE_sys_user'].update({'user_id': state['TABLE_doctor'].get({'slmc_reg_no': argv['Op_Doctor_updateAccountInfo_run_8447']['id']}, 'user_id')}, {'person_id': sys_user_person_id, 'user_id': sys_user_user_id, 'user_name': sys_user_user_name, 'user_type': sys_user_user_type, 'other_info': sys_user_other_info, 'password': sys_user_password, 'online': sys_user_online, 'login': sys_user_login, 'logout': sys_user_logout, 'profile_pic': sys_user_profile_pic, 'suspend': sys_user_suspend})
        return state


class Op_LabAssistant_completeBloodCount_run_8448():
    def __init__(self):
        self.sops = [(self.cond0, self.csop0, self.sop0)]
        self.axiom = AxiomEmpty()

    def cond0(self, state, argv):
        newTstId = argv['Op_LabAssistant_completeBloodCount_run_8448']['newTstId']
        appId = argv['Op_LabAssistant_completeBloodCount_run_8448']['appId']
        totalWhiteCellCount = argv['Op_LabAssistant_completeBloodCount_run_8448']['totalWhiteCellCount']
        differentialCount = argv['Op_LabAssistant_completeBloodCount_run_8448']['differentialCount']
        neutrophils = argv['Op_LabAssistant_completeBloodCount_run_8448']['neutrophils']
        lymphocytes = argv['Op_LabAssistant_completeBloodCount_run_8448']['lymphocytes']
        monocytes = argv['Op_LabAssistant_completeBloodCount_run_8448']['monocytes']
        eosonophils = argv['Op_LabAssistant_completeBloodCount_run_8448']['eosonophils']
        basophils = argv['Op_LabAssistant_completeBloodCount_run_8448']['basophils']
        haemoglobin = argv['Op_LabAssistant_completeBloodCount_run_8448']['haemoglobin']
        redBloodCells = argv['Op_LabAssistant_completeBloodCount_run_8448']['redBloodCells']
        meanCellVolume = argv['Op_LabAssistant_completeBloodCount_run_8448']['meanCellVolume']
        haematocrit = argv['Op_LabAssistant_completeBloodCount_run_8448']['haematocrit']
        meanCellHaemoglobin = argv['Op_LabAssistant_completeBloodCount_run_8448']['meanCellHaemoglobin']
        mchConcentration = argv['Op_LabAssistant_completeBloodCount_run_8448']['mchConcentration']
        redCellsDistributionWidth = argv['Op_LabAssistant_completeBloodCount_run_8448']['redCellsDistributionWidth']
        plateletCount = argv['Op_LabAssistant_completeBloodCount_run_8448']['plateletCount']
        now = argv['Op_LabAssistant_completeBloodCount_run_8448']['now']
        return (state['TABLE_completeBloodCount'].notNil({'tst_CBC_id': argv['Op_LabAssistant_completeBloodCount_run_8448']['newTstId']}) == False)

    def csop0(self, state, argv):
        return True

    def sop0(self, state, argv):
        newTstId = argv['Op_LabAssistant_completeBloodCount_run_8448']['newTstId']
        appId = argv['Op_LabAssistant_completeBloodCount_run_8448']['appId']
        totalWhiteCellCount = argv['Op_LabAssistant_completeBloodCount_run_8448']['totalWhiteCellCount']
        differentialCount = argv['Op_LabAssistant_completeBloodCount_run_8448']['differentialCount']
        neutrophils = argv['Op_LabAssistant_completeBloodCount_run_8448']['neutrophils']
        lymphocytes = argv['Op_LabAssistant_completeBloodCount_run_8448']['lymphocytes']
        monocytes = argv['Op_LabAssistant_completeBloodCount_run_8448']['monocytes']
        eosonophils = argv['Op_LabAssistant_completeBloodCount_run_8448']['eosonophils']
        basophils = argv['Op_LabAssistant_completeBloodCount_run_8448']['basophils']
        haemoglobin = argv['Op_LabAssistant_completeBloodCount_run_8448']['haemoglobin']
        redBloodCells = argv['Op_LabAssistant_completeBloodCount_run_8448']['redBloodCells']
        meanCellVolume = argv['Op_LabAssistant_completeBloodCount_run_8448']['meanCellVolume']
        haematocrit = argv['Op_LabAssistant_completeBloodCount_run_8448']['haematocrit']
        meanCellHaemoglobin = argv['Op_LabAssistant_completeBloodCount_run_8448']['meanCellHaemoglobin']
        mchConcentration = argv['Op_LabAssistant_completeBloodCount_run_8448']['mchConcentration']
        redCellsDistributionWidth = argv['Op_LabAssistant_completeBloodCount_run_8448']['redCellsDistributionWidth']
        plateletCount = argv['Op_LabAssistant_completeBloodCount_run_8448']['plateletCount']
        now = argv['Op_LabAssistant_completeBloodCount_run_8448']['now']
        completeBloodCount_tst_CBC_id = argv['Op_LabAssistant_completeBloodCount_run_8448']['newTstId']
        completeBloodCount_appointment_id = argv['Op_LabAssistant_completeBloodCount_run_8448']['appId']
        completeBloodCount_totalWhiteCellCount = argv['Op_LabAssistant_completeBloodCount_run_8448']['totalWhiteCellCount']
        completeBloodCount_differentialCount = argv['Op_LabAssistant_completeBloodCount_run_8448']['differentialCount']
        completeBloodCount_neutrophils = argv['Op_LabAssistant_completeBloodCount_run_8448']['neutrophils']
        completeBloodCount_lymphocytes = argv['Op_LabAssistant_completeBloodCount_run_8448']['lymphocytes']
        completeBloodCount_monocytes = argv['Op_LabAssistant_completeBloodCount_run_8448']['monocytes']
        completeBloodCount_eosonophils = argv['Op_LabAssistant_completeBloodCount_run_8448']['eosonophils']
        completeBloodCount_basophils = argv['Op_LabAssistant_completeBloodCount_run_8448']['basophils']
        completeBloodCount_haemoglobin = argv['Op_LabAssistant_completeBloodCount_run_8448']['haemoglobin']
        completeBloodCount_redBloodCells = argv['Op_LabAssistant_completeBloodCount_run_8448']['redBloodCells']
        completeBloodCount_meanCellVolume = argv['Op_LabAssistant_completeBloodCount_run_8448']['meanCellVolume']
        completeBloodCount_haematocrit = argv['Op_LabAssistant_completeBloodCount_run_8448']['haematocrit']
        completeBloodCount_meanCellHaemoglobin = argv['Op_LabAssistant_completeBloodCount_run_8448']['meanCellHaemoglobin']
        completeBloodCount_mchConcentration = argv['Op_LabAssistant_completeBloodCount_run_8448']['mchConcentration']
        completeBloodCount_redCellsDistributionWidth = argv['Op_LabAssistant_completeBloodCount_run_8448']['redCellsDistributionWidth']
        completeBloodCount_plateletCount = argv['Op_LabAssistant_completeBloodCount_run_8448']['plateletCount']
        completeBloodCount_date = argv['Op_LabAssistant_completeBloodCount_run_8448']['now']
        state['TABLE_completeBloodCount'].add({'tst_CBC_id': completeBloodCount_tst_CBC_id}, {'appointment_id': completeBloodCount_appointment_id,'totalWhiteCellCount': completeBloodCount_totalWhiteCellCount,'differentialCount': completeBloodCount_differentialCount,'neutrophils': completeBloodCount_neutrophils,'lymphocytes': completeBloodCount_lymphocytes,'monocytes': completeBloodCount_monocytes,'eosonophils': completeBloodCount_eosonophils,'basophils': completeBloodCount_basophils,'haemoglobin': completeBloodCount_haemoglobin,'redBloodCells': completeBloodCount_redBloodCells,'meanCellVolume': completeBloodCount_meanCellVolume,'haematocrit': completeBloodCount_haematocrit,'meanCellHaemoglobin': completeBloodCount_meanCellHaemoglobin,'mchConcentration': completeBloodCount_mchConcentration,'redCellsDistributionWidth': completeBloodCount_redCellsDistributionWidth,'plateletCount': completeBloodCount_plateletCount,'date': completeBloodCount_date})
        return state


class Op_Receptionist_makeAppointment_run_8449():
    def __init__(self):
        self.sops = [(self.cond0, self.csop0, self.sop0), (self.cond1, self.csop1, self.sop1), (self.cond2, self.csop2, self.sop2), (self.cond3, self.csop3, self.sop3), (self.cond4, self.csop4, self.sop4), (self.cond5, self.csop5, self.sop5), (self.cond6, self.csop6, self.sop6)]
        self.axiom = AxiomEmpty()

    def cond0(self, state, argv):
        newAppId = argv['Op_Receptionist_makeAppointment_run_8449']['newAppId']
        patientId = argv['Op_Receptionist_makeAppointment_run_8449']['patientId']
        doctorId = argv['Op_Receptionist_makeAppointment_run_8449']['doctorId']
        currentDate = argv['Op_Receptionist_makeAppointment_run_8449']['currentDate']
        day = argv['Op_Receptionist_makeAppointment_run_8449']['day']
        newAppId = argv['Op_Receptionist_makeAppointment_run_8449']['newAppId']
        patientId = argv['Op_Receptionist_makeAppointment_run_8449']['patientId']
        doctorId = argv['Op_Receptionist_makeAppointment_run_8449']['doctorId']
        currentDate = argv['Op_Receptionist_makeAppointment_run_8449']['currentDate']
        day = argv['Op_Receptionist_makeAppointment_run_8449']['day']
        timeSlot = argv['Op_Receptionist_makeAppointment_run_8449']['timeSlot']
        doctor_availability_time_slot = argv['Op_Receptionist_makeAppointment_run_8449']['doctor_availability_time_slot']
        doctor_availability_slmc_reg_no = argv['Op_Receptionist_makeAppointment_run_8449']['doctor_availability_slmc_reg_no']
        doctor_availability_day = argv['Op_Receptionist_makeAppointment_run_8449']['doctor_availability_day']
        newAppId = argv['Op_Receptionist_makeAppointment_run_8449']['newAppId']
        patientId = argv['Op_Receptionist_makeAppointment_run_8449']['patientId']
        doctorId = argv['Op_Receptionist_makeAppointment_run_8449']['doctorId']
        currentDate = argv['Op_Receptionist_makeAppointment_run_8449']['currentDate']
        day = argv['Op_Receptionist_makeAppointment_run_8449']['day']
        timeSlot = argv['Op_Receptionist_makeAppointment_run_8449']['timeSlot']
        doctor_availability_time_slot = argv['Op_Receptionist_makeAppointment_run_8449']['doctor_availability_time_slot']
        doctor_availability_slmc_reg_no = argv['Op_Receptionist_makeAppointment_run_8449']['doctor_availability_slmc_reg_no']
        doctor_availability_day = argv['Op_Receptionist_makeAppointment_run_8449']['doctor_availability_day']
        newAppId = argv['Op_Receptionist_makeAppointment_run_8449']['newAppId']
        patientId = argv['Op_Receptionist_makeAppointment_run_8449']['patientId']
        doctorId = argv['Op_Receptionist_makeAppointment_run_8449']['doctorId']
        currentDate = argv['Op_Receptionist_makeAppointment_run_8449']['currentDate']
        day = argv['Op_Receptionist_makeAppointment_run_8449']['day']
        timeSlot = argv['Op_Receptionist_makeAppointment_run_8449']['timeSlot']
        doctor_availability_time_slot = argv['Op_Receptionist_makeAppointment_run_8449']['doctor_availability_time_slot']
        doctor_availability_slmc_reg_no = argv['Op_Receptionist_makeAppointment_run_8449']['doctor_availability_slmc_reg_no']
        doctor_availability_day = argv['Op_Receptionist_makeAppointment_run_8449']['doctor_availability_day']
        tmp_bill_tmp_bill_id = argv['Op_Receptionist_makeAppointment_run_8449']['tmp_bill_tmp_bill_id']
        newAppId = argv['Op_Receptionist_makeAppointment_run_8449']['newAppId']
        patientId = argv['Op_Receptionist_makeAppointment_run_8449']['patientId']
        doctorId = argv['Op_Receptionist_makeAppointment_run_8449']['doctorId']
        currentDate = argv['Op_Receptionist_makeAppointment_run_8449']['currentDate']
        day = argv['Op_Receptionist_makeAppointment_run_8449']['day']
        timeSlot = argv['Op_Receptionist_makeAppointment_run_8449']['timeSlot']
        doctor_availability_time_slot = argv['Op_Receptionist_makeAppointment_run_8449']['doctor_availability_time_slot']
        doctor_availability_slmc_reg_no = argv['Op_Receptionist_makeAppointment_run_8449']['doctor_availability_slmc_reg_no']
        doctor_availability_day = argv['Op_Receptionist_makeAppointment_run_8449']['doctor_availability_day']
        tmp_bill_tmp_bill_id = argv['Op_Receptionist_makeAppointment_run_8449']['tmp_bill_tmp_bill_id']
        newAppId = argv['Op_Receptionist_makeAppointment_run_8449']['newAppId']
        patientId = argv['Op_Receptionist_makeAppointment_run_8449']['patientId']
        doctorId = argv['Op_Receptionist_makeAppointment_run_8449']['doctorId']
        currentDate = argv['Op_Receptionist_makeAppointment_run_8449']['currentDate']
        day = argv['Op_Receptionist_makeAppointment_run_8449']['day']
        timeSlot = argv['Op_Receptionist_makeAppointment_run_8449']['timeSlot']
        doctor_availability_time_slot = argv['Op_Receptionist_makeAppointment_run_8449']['doctor_availability_time_slot']
        doctor_availability_slmc_reg_no = argv['Op_Receptionist_makeAppointment_run_8449']['doctor_availability_slmc_reg_no']
        doctor_availability_day = argv['Op_Receptionist_makeAppointment_run_8449']['doctor_availability_day']
        newTmpBillId = argv['Op_Receptionist_makeAppointment_run_8449']['newTmpBillId']
        newAppId = argv['Op_Receptionist_makeAppointment_run_8449']['newAppId']
        patientId = argv['Op_Receptionist_makeAppointment_run_8449']['patientId']
        doctorId = argv['Op_Receptionist_makeAppointment_run_8449']['doctorId']
        currentDate = argv['Op_Receptionist_makeAppointment_run_8449']['currentDate']
        day = argv['Op_Receptionist_makeAppointment_run_8449']['day']
        timeSlot = argv['Op_Receptionist_makeAppointment_run_8449']['timeSlot']
        doctor_availability_time_slot = argv['Op_Receptionist_makeAppointment_run_8449']['doctor_availability_time_slot']
        doctor_availability_slmc_reg_no = argv['Op_Receptionist_makeAppointment_run_8449']['doctor_availability_slmc_reg_no']
        doctor_availability_day = argv['Op_Receptionist_makeAppointment_run_8449']['doctor_availability_day']
        newTmpBillId = argv['Op_Receptionist_makeAppointment_run_8449']['newTmpBillId']
        return And((state['TABLE_appointment'].notNil({'appointment_id': argv['Op_Receptionist_makeAppointment_run_8449']['newAppId']}) == False),Not((state['TABLE_appointment'].notNil({'appointment_id': argv['Op_Receptionist_makeAppointment_run_8449']['newAppId']}) == False)),Not((argv['Op_Receptionist_makeAppointment_run_8449']['day'])<=(3631)),Not((state['TABLE_doctor_availability'].notNil({'time_slot': argv['Op_Receptionist_makeAppointment_run_8449']['timeSlot'], 'slmc_reg_no': argv['Op_Receptionist_makeAppointment_run_8449']['doctorId'], 'day': argv['Op_Receptionist_makeAppointment_run_8449']['day']}) == True)),Not((state['TABLE_appointment'].notNil({'appointment_id': argv['Op_Receptionist_makeAppointment_run_8449']['newAppId']}) == False)),Not((argv['Op_Receptionist_makeAppointment_run_8449']['day'])<=(3631)),Not((state['TABLE_doctor_availability'].notNil({'time_slot': argv['Op_Receptionist_makeAppointment_run_8449']['timeSlot'], 'slmc_reg_no': argv['Op_Receptionist_makeAppointment_run_8449']['doctorId'], 'day': argv['Op_Receptionist_makeAppointment_run_8449']['day']}) == True)),Not((state['TABLE_appointment'].notNil({'appointment_id': argv['Op_Receptionist_makeAppointment_run_8449']['newAppId']}) == False)),Not((argv['Op_Receptionist_makeAppointment_run_8449']['day'])<=(3631)),Not((state['TABLE_doctor_availability'].notNil({'time_slot': argv['Op_Receptionist_makeAppointment_run_8449']['timeSlot'], 'slmc_reg_no': argv['Op_Receptionist_makeAppointment_run_8449']['doctorId'], 'day': argv['Op_Receptionist_makeAppointment_run_8449']['day']}) == True)),Not((state['TABLE_tmp_bill'].notNil({'patient_id': argv['Op_Receptionist_makeAppointment_run_8449']['patientId']}) == True)),Not((state['TABLE_tmp_bill'].notNil({'tmp_bill_id': state['TABLE_tmp_bill'].get({'patient_id': argv['Op_Receptionist_makeAppointment_run_8449']['patientId']}, 'tmp_bill_id')}) == True)),Not((state['TABLE_appointment'].notNil({'appointment_id': argv['Op_Receptionist_makeAppointment_run_8449']['newAppId']}) == False)),Not((argv['Op_Receptionist_makeAppointment_run_8449']['day'])<=(3631)),Not((state['TABLE_doctor_availability'].notNil({'time_slot': argv['Op_Receptionist_makeAppointment_run_8449']['timeSlot'], 'slmc_reg_no': argv['Op_Receptionist_makeAppointment_run_8449']['doctorId'], 'day': argv['Op_Receptionist_makeAppointment_run_8449']['day']}) == True)),Not((state['TABLE_tmp_bill'].notNil({'patient_id': argv['Op_Receptionist_makeAppointment_run_8449']['patientId']}) == True)),Not((state['TABLE_tmp_bill'].notNil({'tmp_bill_id': state['TABLE_tmp_bill'].get({'patient_id': argv['Op_Receptionist_makeAppointment_run_8449']['patientId']}, 'tmp_bill_id')}) == True)),Not((state['TABLE_appointment'].notNil({'appointment_id': argv['Op_Receptionist_makeAppointment_run_8449']['newAppId']}) == False)),Not((argv['Op_Receptionist_makeAppointment_run_8449']['day'])<=(3631)),Not((state['TABLE_doctor_availability'].notNil({'time_slot': argv['Op_Receptionist_makeAppointment_run_8449']['timeSlot'], 'slmc_reg_no': argv['Op_Receptionist_makeAppointment_run_8449']['doctorId'], 'day': argv['Op_Receptionist_makeAppointment_run_8449']['day']}) == True)),Not((state['TABLE_tmp_bill'].notNil({'patient_id': argv['Op_Receptionist_makeAppointment_run_8449']['patientId']}) == False)),Not((state['TABLE_appointment'].notNil({'appointment_id': argv['Op_Receptionist_makeAppointment_run_8449']['newAppId']}) == False)),Not((argv['Op_Receptionist_makeAppointment_run_8449']['day'])<=(3631)),Not((state['TABLE_doctor_availability'].notNil({'time_slot': argv['Op_Receptionist_makeAppointment_run_8449']['timeSlot'], 'slmc_reg_no': argv['Op_Receptionist_makeAppointment_run_8449']['doctorId'], 'day': argv['Op_Receptionist_makeAppointment_run_8449']['day']}) == True)),Not((state['TABLE_tmp_bill'].notNil({'patient_id': argv['Op_Receptionist_makeAppointment_run_8449']['patientId']}) == False)))

    def csop0(self, state, argv):
        return True

    def sop0(self, state, argv):
        newAppId = argv['Op_Receptionist_makeAppointment_run_8449']['newAppId']
        patientId = argv['Op_Receptionist_makeAppointment_run_8449']['patientId']
        doctorId = argv['Op_Receptionist_makeAppointment_run_8449']['doctorId']
        currentDate = argv['Op_Receptionist_makeAppointment_run_8449']['currentDate']
        day = argv['Op_Receptionist_makeAppointment_run_8449']['day']
        appointment_appointment_id = argv['Op_Receptionist_makeAppointment_run_8449']['newAppId']
        appointment_patient_id = argv['Op_Receptionist_makeAppointment_run_8449']['patientId']
        appointment_slmc_reg_no = argv['Op_Receptionist_makeAppointment_run_8449']['doctorId']
        appointment_date = (argv['Op_Receptionist_makeAppointment_run_8449']['currentDate'])+(argv['Op_Receptionist_makeAppointment_run_8449']['day'])
        appointment_cancelled = False
        state['TABLE_appointment'].add({'appointment_id': appointment_appointment_id}, {'patient_id': appointment_patient_id,'slmc_reg_no': appointment_slmc_reg_no,'date': appointment_date,'cancelled': appointment_cancelled})
        return state

    def cond1(self, state, argv):
        newAppId = argv['Op_Receptionist_makeAppointment_run_8449']['newAppId']
        patientId = argv['Op_Receptionist_makeAppointment_run_8449']['patientId']
        doctorId = argv['Op_Receptionist_makeAppointment_run_8449']['doctorId']
        currentDate = argv['Op_Receptionist_makeAppointment_run_8449']['currentDate']
        day = argv['Op_Receptionist_makeAppointment_run_8449']['day']
        timeSlot = argv['Op_Receptionist_makeAppointment_run_8449']['timeSlot']
        doctor_availability_time_slot = argv['Op_Receptionist_makeAppointment_run_8449']['doctor_availability_time_slot']
        doctor_availability_slmc_reg_no = argv['Op_Receptionist_makeAppointment_run_8449']['doctor_availability_slmc_reg_no']
        doctor_availability_day = argv['Op_Receptionist_makeAppointment_run_8449']['doctor_availability_day']
        newAppId = argv['Op_Receptionist_makeAppointment_run_8449']['newAppId']
        patientId = argv['Op_Receptionist_makeAppointment_run_8449']['patientId']
        doctorId = argv['Op_Receptionist_makeAppointment_run_8449']['doctorId']
        currentDate = argv['Op_Receptionist_makeAppointment_run_8449']['currentDate']
        day = argv['Op_Receptionist_makeAppointment_run_8449']['day']
        timeSlot = argv['Op_Receptionist_makeAppointment_run_8449']['timeSlot']
        doctor_availability_time_slot = argv['Op_Receptionist_makeAppointment_run_8449']['doctor_availability_time_slot']
        doctor_availability_slmc_reg_no = argv['Op_Receptionist_makeAppointment_run_8449']['doctor_availability_slmc_reg_no']
        doctor_availability_day = argv['Op_Receptionist_makeAppointment_run_8449']['doctor_availability_day']
        tmp_bill_tmp_bill_id = argv['Op_Receptionist_makeAppointment_run_8449']['tmp_bill_tmp_bill_id']
        newAppId = argv['Op_Receptionist_makeAppointment_run_8449']['newAppId']
        patientId = argv['Op_Receptionist_makeAppointment_run_8449']['patientId']
        doctorId = argv['Op_Receptionist_makeAppointment_run_8449']['doctorId']
        currentDate = argv['Op_Receptionist_makeAppointment_run_8449']['currentDate']
        day = argv['Op_Receptionist_makeAppointment_run_8449']['day']
        timeSlot = argv['Op_Receptionist_makeAppointment_run_8449']['timeSlot']
        doctor_availability_time_slot = argv['Op_Receptionist_makeAppointment_run_8449']['doctor_availability_time_slot']
        doctor_availability_slmc_reg_no = argv['Op_Receptionist_makeAppointment_run_8449']['doctor_availability_slmc_reg_no']
        doctor_availability_day = argv['Op_Receptionist_makeAppointment_run_8449']['doctor_availability_day']
        newTmpBillId = argv['Op_Receptionist_makeAppointment_run_8449']['newTmpBillId']
        return And((state['TABLE_appointment'].notNil({'appointment_id': argv['Op_Receptionist_makeAppointment_run_8449']['newAppId']}) == False),(argv['Op_Receptionist_makeAppointment_run_8449']['day'])<=(3631),(state['TABLE_doctor_availability'].notNil({'time_slot': argv['Op_Receptionist_makeAppointment_run_8449']['timeSlot'], 'slmc_reg_no': argv['Op_Receptionist_makeAppointment_run_8449']['doctorId'], 'day': argv['Op_Receptionist_makeAppointment_run_8449']['day']}) == True),Not((state['TABLE_appointment'].notNil({'appointment_id': argv['Op_Receptionist_makeAppointment_run_8449']['newAppId']}) == False)),Not((argv['Op_Receptionist_makeAppointment_run_8449']['day'])<=(3631)),Not((state['TABLE_doctor_availability'].notNil({'time_slot': argv['Op_Receptionist_makeAppointment_run_8449']['timeSlot'], 'slmc_reg_no': argv['Op_Receptionist_makeAppointment_run_8449']['doctorId'], 'day': argv['Op_Receptionist_makeAppointment_run_8449']['day']}) == True)),Not((state['TABLE_tmp_bill'].notNil({'patient_id': argv['Op_Receptionist_makeAppointment_run_8449']['patientId']}) == True)),Not((state['TABLE_tmp_bill'].notNil({'tmp_bill_id': state['TABLE_tmp_bill'].get({'patient_id': argv['Op_Receptionist_makeAppointment_run_8449']['patientId']}, 'tmp_bill_id')}) == True)),Not((state['TABLE_appointment'].notNil({'appointment_id': argv['Op_Receptionist_makeAppointment_run_8449']['newAppId']}) == False)),Not((argv['Op_Receptionist_makeAppointment_run_8449']['day'])<=(3631)),Not((state['TABLE_doctor_availability'].notNil({'time_slot': argv['Op_Receptionist_makeAppointment_run_8449']['timeSlot'], 'slmc_reg_no': argv['Op_Receptionist_makeAppointment_run_8449']['doctorId'], 'day': argv['Op_Receptionist_makeAppointment_run_8449']['day']}) == True)),Not((state['TABLE_tmp_bill'].notNil({'patient_id': argv['Op_Receptionist_makeAppointment_run_8449']['patientId']}) == False)))

    def csop1(self, state, argv):
        return True

    def sop1(self, state, argv):
        newAppId = argv['Op_Receptionist_makeAppointment_run_8449']['newAppId']
        patientId = argv['Op_Receptionist_makeAppointment_run_8449']['patientId']
        doctorId = argv['Op_Receptionist_makeAppointment_run_8449']['doctorId']
        currentDate = argv['Op_Receptionist_makeAppointment_run_8449']['currentDate']
        day = argv['Op_Receptionist_makeAppointment_run_8449']['day']
        timeSlot = argv['Op_Receptionist_makeAppointment_run_8449']['timeSlot']
        doctor_availability_time_slot = argv['Op_Receptionist_makeAppointment_run_8449']['doctor_availability_time_slot']
        doctor_availability_slmc_reg_no = argv['Op_Receptionist_makeAppointment_run_8449']['doctor_availability_slmc_reg_no']
        doctor_availability_day = argv['Op_Receptionist_makeAppointment_run_8449']['doctor_availability_day']
        appointment_appointment_id = argv['Op_Receptionist_makeAppointment_run_8449']['newAppId']
        appointment_patient_id = argv['Op_Receptionist_makeAppointment_run_8449']['patientId']
        appointment_slmc_reg_no = argv['Op_Receptionist_makeAppointment_run_8449']['doctorId']
        appointment_date = (argv['Op_Receptionist_makeAppointment_run_8449']['currentDate'])+(argv['Op_Receptionist_makeAppointment_run_8449']['day'])
        appointment_cancelled = False
        state['TABLE_appointment'].add({'appointment_id': appointment_appointment_id}, {'patient_id': appointment_patient_id,'slmc_reg_no': appointment_slmc_reg_no,'date': appointment_date,'cancelled': appointment_cancelled})
        doctor_availability_time_slot_id = state['TABLE_doctor_availability'].get({'time_slot': argv['Op_Receptionist_makeAppointment_run_8449']['timeSlot'],'slmc_reg_no': argv['Op_Receptionist_makeAppointment_run_8449']['doctorId'],'day': argv['Op_Receptionist_makeAppointment_run_8449']['day']}, 'time_slot_id')
        doctor_availability_slmc_reg_no = state['TABLE_doctor_availability'].get({'time_slot': argv['Op_Receptionist_makeAppointment_run_8449']['timeSlot'],'slmc_reg_no': argv['Op_Receptionist_makeAppointment_run_8449']['doctorId'],'day': argv['Op_Receptionist_makeAppointment_run_8449']['day']}, 'slmc_reg_no')
        doctor_availability_day = state['TABLE_doctor_availability'].get({'time_slot': argv['Op_Receptionist_makeAppointment_run_8449']['timeSlot'],'slmc_reg_no': argv['Op_Receptionist_makeAppointment_run_8449']['doctorId'],'day': argv['Op_Receptionist_makeAppointment_run_8449']['day']}, 'day')
        doctor_availability_time_slot = state['TABLE_doctor_availability'].get({'time_slot': argv['Op_Receptionist_makeAppointment_run_8449']['timeSlot'],'slmc_reg_no': argv['Op_Receptionist_makeAppointment_run_8449']['doctorId'],'day': argv['Op_Receptionist_makeAppointment_run_8449']['day']}, 'time_slot')
        doctor_availability_current_week_appointments = state['TABLE_doctor_availability'].get({'time_slot': argv['Op_Receptionist_makeAppointment_run_8449']['timeSlot'],'slmc_reg_no': argv['Op_Receptionist_makeAppointment_run_8449']['doctorId'],'day': argv['Op_Receptionist_makeAppointment_run_8449']['day']}, 'current_week_appointments')
        doctor_availability_next_week_appointments = state['TABLE_doctor_availability'].get({'time_slot': argv['Op_Receptionist_makeAppointment_run_8449']['timeSlot'],'slmc_reg_no': argv['Op_Receptionist_makeAppointment_run_8449']['doctorId'],'day': argv['Op_Receptionist_makeAppointment_run_8449']['day']}, 'next_week_appointments')
        doctor_availability_current_week_appointments = (doctor_availability_current_week_appointments)+(1)
        state['TABLE_doctor_availability'].update({'time_slot': argv['Op_Receptionist_makeAppointment_run_8449']['timeSlot'],'slmc_reg_no': argv['Op_Receptionist_makeAppointment_run_8449']['doctorId'],'day': argv['Op_Receptionist_makeAppointment_run_8449']['day']}, {'time_slot_id': doctor_availability_time_slot_id, 'slmc_reg_no': doctor_availability_slmc_reg_no, 'day': doctor_availability_day, 'time_slot': doctor_availability_time_slot, 'current_week_appointments': doctor_availability_current_week_appointments, 'next_week_appointments': doctor_availability_next_week_appointments})
        return state

    def cond2(self, state, argv):
        newAppId = argv['Op_Receptionist_makeAppointment_run_8449']['newAppId']
        patientId = argv['Op_Receptionist_makeAppointment_run_8449']['patientId']
        doctorId = argv['Op_Receptionist_makeAppointment_run_8449']['doctorId']
        currentDate = argv['Op_Receptionist_makeAppointment_run_8449']['currentDate']
        day = argv['Op_Receptionist_makeAppointment_run_8449']['day']
        timeSlot = argv['Op_Receptionist_makeAppointment_run_8449']['timeSlot']
        doctor_availability_time_slot = argv['Op_Receptionist_makeAppointment_run_8449']['doctor_availability_time_slot']
        doctor_availability_slmc_reg_no = argv['Op_Receptionist_makeAppointment_run_8449']['doctor_availability_slmc_reg_no']
        doctor_availability_day = argv['Op_Receptionist_makeAppointment_run_8449']['doctor_availability_day']
        newAppId = argv['Op_Receptionist_makeAppointment_run_8449']['newAppId']
        patientId = argv['Op_Receptionist_makeAppointment_run_8449']['patientId']
        doctorId = argv['Op_Receptionist_makeAppointment_run_8449']['doctorId']
        currentDate = argv['Op_Receptionist_makeAppointment_run_8449']['currentDate']
        day = argv['Op_Receptionist_makeAppointment_run_8449']['day']
        timeSlot = argv['Op_Receptionist_makeAppointment_run_8449']['timeSlot']
        doctor_availability_time_slot = argv['Op_Receptionist_makeAppointment_run_8449']['doctor_availability_time_slot']
        doctor_availability_slmc_reg_no = argv['Op_Receptionist_makeAppointment_run_8449']['doctor_availability_slmc_reg_no']
        doctor_availability_day = argv['Op_Receptionist_makeAppointment_run_8449']['doctor_availability_day']
        tmp_bill_tmp_bill_id = argv['Op_Receptionist_makeAppointment_run_8449']['tmp_bill_tmp_bill_id']
        newAppId = argv['Op_Receptionist_makeAppointment_run_8449']['newAppId']
        patientId = argv['Op_Receptionist_makeAppointment_run_8449']['patientId']
        doctorId = argv['Op_Receptionist_makeAppointment_run_8449']['doctorId']
        currentDate = argv['Op_Receptionist_makeAppointment_run_8449']['currentDate']
        day = argv['Op_Receptionist_makeAppointment_run_8449']['day']
        timeSlot = argv['Op_Receptionist_makeAppointment_run_8449']['timeSlot']
        doctor_availability_time_slot = argv['Op_Receptionist_makeAppointment_run_8449']['doctor_availability_time_slot']
        doctor_availability_slmc_reg_no = argv['Op_Receptionist_makeAppointment_run_8449']['doctor_availability_slmc_reg_no']
        doctor_availability_day = argv['Op_Receptionist_makeAppointment_run_8449']['doctor_availability_day']
        newTmpBillId = argv['Op_Receptionist_makeAppointment_run_8449']['newTmpBillId']
        return And((state['TABLE_appointment'].notNil({'appointment_id': argv['Op_Receptionist_makeAppointment_run_8449']['newAppId']}) == False),(argv['Op_Receptionist_makeAppointment_run_8449']['day'])<=(3631),(state['TABLE_doctor_availability'].notNil({'time_slot': argv['Op_Receptionist_makeAppointment_run_8449']['timeSlot'], 'slmc_reg_no': argv['Op_Receptionist_makeAppointment_run_8449']['doctorId'], 'day': argv['Op_Receptionist_makeAppointment_run_8449']['day']}) == True),Not((state['TABLE_appointment'].notNil({'appointment_id': argv['Op_Receptionist_makeAppointment_run_8449']['newAppId']}) == False)),Not((argv['Op_Receptionist_makeAppointment_run_8449']['day'])<=(3631)),Not((state['TABLE_doctor_availability'].notNil({'time_slot': argv['Op_Receptionist_makeAppointment_run_8449']['timeSlot'], 'slmc_reg_no': argv['Op_Receptionist_makeAppointment_run_8449']['doctorId'], 'day': argv['Op_Receptionist_makeAppointment_run_8449']['day']}) == True)),Not((state['TABLE_tmp_bill'].notNil({'patient_id': argv['Op_Receptionist_makeAppointment_run_8449']['patientId']}) == True)),Not((state['TABLE_tmp_bill'].notNil({'tmp_bill_id': state['TABLE_tmp_bill'].get({'patient_id': argv['Op_Receptionist_makeAppointment_run_8449']['patientId']}, 'tmp_bill_id')}) == True)),Not((state['TABLE_appointment'].notNil({'appointment_id': argv['Op_Receptionist_makeAppointment_run_8449']['newAppId']}) == False)),Not((argv['Op_Receptionist_makeAppointment_run_8449']['day'])<=(3631)),Not((state['TABLE_doctor_availability'].notNil({'time_slot': argv['Op_Receptionist_makeAppointment_run_8449']['timeSlot'], 'slmc_reg_no': argv['Op_Receptionist_makeAppointment_run_8449']['doctorId'], 'day': argv['Op_Receptionist_makeAppointment_run_8449']['day']}) == True)),Not((state['TABLE_tmp_bill'].notNil({'patient_id': argv['Op_Receptionist_makeAppointment_run_8449']['patientId']}) == False)))

    def csop2(self, state, argv):
        return True

    def sop2(self, state, argv):
        newAppId = argv['Op_Receptionist_makeAppointment_run_8449']['newAppId']
        patientId = argv['Op_Receptionist_makeAppointment_run_8449']['patientId']
        doctorId = argv['Op_Receptionist_makeAppointment_run_8449']['doctorId']
        currentDate = argv['Op_Receptionist_makeAppointment_run_8449']['currentDate']
        day = argv['Op_Receptionist_makeAppointment_run_8449']['day']
        timeSlot = argv['Op_Receptionist_makeAppointment_run_8449']['timeSlot']
        doctor_availability_time_slot = argv['Op_Receptionist_makeAppointment_run_8449']['doctor_availability_time_slot']
        doctor_availability_slmc_reg_no = argv['Op_Receptionist_makeAppointment_run_8449']['doctor_availability_slmc_reg_no']
        doctor_availability_day = argv['Op_Receptionist_makeAppointment_run_8449']['doctor_availability_day']
        appointment_appointment_id = argv['Op_Receptionist_makeAppointment_run_8449']['newAppId']
        appointment_patient_id = argv['Op_Receptionist_makeAppointment_run_8449']['patientId']
        appointment_slmc_reg_no = argv['Op_Receptionist_makeAppointment_run_8449']['doctorId']
        appointment_date = (argv['Op_Receptionist_makeAppointment_run_8449']['currentDate'])+(argv['Op_Receptionist_makeAppointment_run_8449']['day'])
        appointment_cancelled = False
        state['TABLE_appointment'].add({'appointment_id': appointment_appointment_id}, {'patient_id': appointment_patient_id,'slmc_reg_no': appointment_slmc_reg_no,'date': appointment_date,'cancelled': appointment_cancelled})
        doctor_availability_time_slot_id = state['TABLE_doctor_availability'].get({'time_slot': argv['Op_Receptionist_makeAppointment_run_8449']['timeSlot'],'slmc_reg_no': argv['Op_Receptionist_makeAppointment_run_8449']['doctorId'],'day': argv['Op_Receptionist_makeAppointment_run_8449']['day']}, 'time_slot_id')
        doctor_availability_slmc_reg_no = state['TABLE_doctor_availability'].get({'time_slot': argv['Op_Receptionist_makeAppointment_run_8449']['timeSlot'],'slmc_reg_no': argv['Op_Receptionist_makeAppointment_run_8449']['doctorId'],'day': argv['Op_Receptionist_makeAppointment_run_8449']['day']}, 'slmc_reg_no')
        doctor_availability_day = state['TABLE_doctor_availability'].get({'time_slot': argv['Op_Receptionist_makeAppointment_run_8449']['timeSlot'],'slmc_reg_no': argv['Op_Receptionist_makeAppointment_run_8449']['doctorId'],'day': argv['Op_Receptionist_makeAppointment_run_8449']['day']}, 'day')
        doctor_availability_time_slot = state['TABLE_doctor_availability'].get({'time_slot': argv['Op_Receptionist_makeAppointment_run_8449']['timeSlot'],'slmc_reg_no': argv['Op_Receptionist_makeAppointment_run_8449']['doctorId'],'day': argv['Op_Receptionist_makeAppointment_run_8449']['day']}, 'time_slot')
        doctor_availability_current_week_appointments = state['TABLE_doctor_availability'].get({'time_slot': argv['Op_Receptionist_makeAppointment_run_8449']['timeSlot'],'slmc_reg_no': argv['Op_Receptionist_makeAppointment_run_8449']['doctorId'],'day': argv['Op_Receptionist_makeAppointment_run_8449']['day']}, 'current_week_appointments')
        doctor_availability_next_week_appointments = state['TABLE_doctor_availability'].get({'time_slot': argv['Op_Receptionist_makeAppointment_run_8449']['timeSlot'],'slmc_reg_no': argv['Op_Receptionist_makeAppointment_run_8449']['doctorId'],'day': argv['Op_Receptionist_makeAppointment_run_8449']['day']}, 'next_week_appointments')
        doctor_availability_next_week_appointments = (doctor_availability_next_week_appointments)+(1)
        state['TABLE_doctor_availability'].update({'time_slot': argv['Op_Receptionist_makeAppointment_run_8449']['timeSlot'],'slmc_reg_no': argv['Op_Receptionist_makeAppointment_run_8449']['doctorId'],'day': argv['Op_Receptionist_makeAppointment_run_8449']['day']}, {'time_slot_id': doctor_availability_time_slot_id, 'slmc_reg_no': doctor_availability_slmc_reg_no, 'day': doctor_availability_day, 'time_slot': doctor_availability_time_slot, 'current_week_appointments': doctor_availability_current_week_appointments, 'next_week_appointments': doctor_availability_next_week_appointments})
        return state

    def cond3(self, state, argv):
        newAppId = argv['Op_Receptionist_makeAppointment_run_8449']['newAppId']
        patientId = argv['Op_Receptionist_makeAppointment_run_8449']['patientId']
        doctorId = argv['Op_Receptionist_makeAppointment_run_8449']['doctorId']
        currentDate = argv['Op_Receptionist_makeAppointment_run_8449']['currentDate']
        day = argv['Op_Receptionist_makeAppointment_run_8449']['day']
        timeSlot = argv['Op_Receptionist_makeAppointment_run_8449']['timeSlot']
        doctor_availability_time_slot = argv['Op_Receptionist_makeAppointment_run_8449']['doctor_availability_time_slot']
        doctor_availability_slmc_reg_no = argv['Op_Receptionist_makeAppointment_run_8449']['doctor_availability_slmc_reg_no']
        doctor_availability_day = argv['Op_Receptionist_makeAppointment_run_8449']['doctor_availability_day']
        tmp_bill_tmp_bill_id = argv['Op_Receptionist_makeAppointment_run_8449']['tmp_bill_tmp_bill_id']
        return And((state['TABLE_appointment'].notNil({'appointment_id': argv['Op_Receptionist_makeAppointment_run_8449']['newAppId']}) == False),(argv['Op_Receptionist_makeAppointment_run_8449']['day'])<=(3631),(state['TABLE_doctor_availability'].notNil({'time_slot': argv['Op_Receptionist_makeAppointment_run_8449']['timeSlot'], 'slmc_reg_no': argv['Op_Receptionist_makeAppointment_run_8449']['doctorId'], 'day': argv['Op_Receptionist_makeAppointment_run_8449']['day']}) == True),(state['TABLE_tmp_bill'].notNil({'patient_id': argv['Op_Receptionist_makeAppointment_run_8449']['patientId']}) == True),(state['TABLE_tmp_bill'].notNil({'tmp_bill_id': state['TABLE_tmp_bill'].get({'patient_id': argv['Op_Receptionist_makeAppointment_run_8449']['patientId']}, 'tmp_bill_id')}) == True))

    def csop3(self, state, argv):
        return True

    def sop3(self, state, argv):
        newAppId = argv['Op_Receptionist_makeAppointment_run_8449']['newAppId']
        patientId = argv['Op_Receptionist_makeAppointment_run_8449']['patientId']
        doctorId = argv['Op_Receptionist_makeAppointment_run_8449']['doctorId']
        currentDate = argv['Op_Receptionist_makeAppointment_run_8449']['currentDate']
        day = argv['Op_Receptionist_makeAppointment_run_8449']['day']
        timeSlot = argv['Op_Receptionist_makeAppointment_run_8449']['timeSlot']
        doctor_availability_time_slot = argv['Op_Receptionist_makeAppointment_run_8449']['doctor_availability_time_slot']
        doctor_availability_slmc_reg_no = argv['Op_Receptionist_makeAppointment_run_8449']['doctor_availability_slmc_reg_no']
        doctor_availability_day = argv['Op_Receptionist_makeAppointment_run_8449']['doctor_availability_day']
        tmp_bill_tmp_bill_id = argv['Op_Receptionist_makeAppointment_run_8449']['tmp_bill_tmp_bill_id']
        appointment_appointment_id = argv['Op_Receptionist_makeAppointment_run_8449']['newAppId']
        appointment_patient_id = argv['Op_Receptionist_makeAppointment_run_8449']['patientId']
        appointment_slmc_reg_no = argv['Op_Receptionist_makeAppointment_run_8449']['doctorId']
        appointment_date = (argv['Op_Receptionist_makeAppointment_run_8449']['currentDate'])+(argv['Op_Receptionist_makeAppointment_run_8449']['day'])
        appointment_cancelled = False
        state['TABLE_appointment'].add({'appointment_id': appointment_appointment_id}, {'patient_id': appointment_patient_id,'slmc_reg_no': appointment_slmc_reg_no,'date': appointment_date,'cancelled': appointment_cancelled})
        doctor_availability_time_slot_id = state['TABLE_doctor_availability'].get({'time_slot': argv['Op_Receptionist_makeAppointment_run_8449']['timeSlot'],'slmc_reg_no': argv['Op_Receptionist_makeAppointment_run_8449']['doctorId'],'day': argv['Op_Receptionist_makeAppointment_run_8449']['day']}, 'time_slot_id')
        doctor_availability_slmc_reg_no = state['TABLE_doctor_availability'].get({'time_slot': argv['Op_Receptionist_makeAppointment_run_8449']['timeSlot'],'slmc_reg_no': argv['Op_Receptionist_makeAppointment_run_8449']['doctorId'],'day': argv['Op_Receptionist_makeAppointment_run_8449']['day']}, 'slmc_reg_no')
        doctor_availability_day = state['TABLE_doctor_availability'].get({'time_slot': argv['Op_Receptionist_makeAppointment_run_8449']['timeSlot'],'slmc_reg_no': argv['Op_Receptionist_makeAppointment_run_8449']['doctorId'],'day': argv['Op_Receptionist_makeAppointment_run_8449']['day']}, 'day')
        doctor_availability_time_slot = state['TABLE_doctor_availability'].get({'time_slot': argv['Op_Receptionist_makeAppointment_run_8449']['timeSlot'],'slmc_reg_no': argv['Op_Receptionist_makeAppointment_run_8449']['doctorId'],'day': argv['Op_Receptionist_makeAppointment_run_8449']['day']}, 'time_slot')
        doctor_availability_current_week_appointments = state['TABLE_doctor_availability'].get({'time_slot': argv['Op_Receptionist_makeAppointment_run_8449']['timeSlot'],'slmc_reg_no': argv['Op_Receptionist_makeAppointment_run_8449']['doctorId'],'day': argv['Op_Receptionist_makeAppointment_run_8449']['day']}, 'current_week_appointments')
        doctor_availability_next_week_appointments = state['TABLE_doctor_availability'].get({'time_slot': argv['Op_Receptionist_makeAppointment_run_8449']['timeSlot'],'slmc_reg_no': argv['Op_Receptionist_makeAppointment_run_8449']['doctorId'],'day': argv['Op_Receptionist_makeAppointment_run_8449']['day']}, 'next_week_appointments')
        doctor_availability_current_week_appointments = (doctor_availability_current_week_appointments)+(1)
        state['TABLE_doctor_availability'].update({'time_slot': argv['Op_Receptionist_makeAppointment_run_8449']['timeSlot'],'slmc_reg_no': argv['Op_Receptionist_makeAppointment_run_8449']['doctorId'],'day': argv['Op_Receptionist_makeAppointment_run_8449']['day']}, {'time_slot_id': doctor_availability_time_slot_id, 'slmc_reg_no': doctor_availability_slmc_reg_no, 'day': doctor_availability_day, 'time_slot': doctor_availability_time_slot, 'current_week_appointments': doctor_availability_current_week_appointments, 'next_week_appointments': doctor_availability_next_week_appointments})
        tmp_bill_tmp_bill_id = state['TABLE_tmp_bill'].get({'tmp_bill_id': state['TABLE_tmp_bill'].get({'patient_id': argv['Op_Receptionist_makeAppointment_run_8449']['patientId']}, 'tmp_bill_id')}, 'tmp_bill_id')
        tmp_bill_doctor_fee = state['TABLE_tmp_bill'].get({'tmp_bill_id': state['TABLE_tmp_bill'].get({'patient_id': argv['Op_Receptionist_makeAppointment_run_8449']['patientId']}, 'tmp_bill_id')}, 'doctor_fee')
        tmp_bill_hospital_fee = state['TABLE_tmp_bill'].get({'tmp_bill_id': state['TABLE_tmp_bill'].get({'patient_id': argv['Op_Receptionist_makeAppointment_run_8449']['patientId']}, 'tmp_bill_id')}, 'hospital_fee')
        tmp_bill_pharmacy_fee = state['TABLE_tmp_bill'].get({'tmp_bill_id': state['TABLE_tmp_bill'].get({'patient_id': argv['Op_Receptionist_makeAppointment_run_8449']['patientId']}, 'tmp_bill_id')}, 'pharmacy_fee')
        tmp_bill_laboratory_fee = state['TABLE_tmp_bill'].get({'tmp_bill_id': state['TABLE_tmp_bill'].get({'patient_id': argv['Op_Receptionist_makeAppointment_run_8449']['patientId']}, 'tmp_bill_id')}, 'laboratory_fee')
        tmp_bill_appointment_fee = state['TABLE_tmp_bill'].get({'tmp_bill_id': state['TABLE_tmp_bill'].get({'patient_id': argv['Op_Receptionist_makeAppointment_run_8449']['patientId']}, 'tmp_bill_id')}, 'appointment_fee')
        tmp_bill_vat = state['TABLE_tmp_bill'].get({'tmp_bill_id': state['TABLE_tmp_bill'].get({'patient_id': argv['Op_Receptionist_makeAppointment_run_8449']['patientId']}, 'tmp_bill_id')}, 'vat')
        tmp_bill_discount = state['TABLE_tmp_bill'].get({'tmp_bill_id': state['TABLE_tmp_bill'].get({'patient_id': argv['Op_Receptionist_makeAppointment_run_8449']['patientId']}, 'tmp_bill_id')}, 'discount')
        tmp_bill_consultant_id = state['TABLE_tmp_bill'].get({'tmp_bill_id': state['TABLE_tmp_bill'].get({'patient_id': argv['Op_Receptionist_makeAppointment_run_8449']['patientId']}, 'tmp_bill_id')}, 'consultant_id')
        tmp_bill_patient_id = state['TABLE_tmp_bill'].get({'tmp_bill_id': state['TABLE_tmp_bill'].get({'patient_id': argv['Op_Receptionist_makeAppointment_run_8449']['patientId']}, 'tmp_bill_id')}, 'patient_id')
        tmp_bill_appointment_fee = 500
        state['TABLE_tmp_bill'].update({'tmp_bill_id': state['TABLE_tmp_bill'].get({'patient_id': argv['Op_Receptionist_makeAppointment_run_8449']['patientId']}, 'tmp_bill_id')}, {'tmp_bill_id': tmp_bill_tmp_bill_id, 'doctor_fee': tmp_bill_doctor_fee, 'hospital_fee': tmp_bill_hospital_fee, 'pharmacy_fee': tmp_bill_pharmacy_fee, 'laboratory_fee': tmp_bill_laboratory_fee, 'appointment_fee': tmp_bill_appointment_fee, 'vat': tmp_bill_vat, 'discount': tmp_bill_discount, 'consultant_id': tmp_bill_consultant_id, 'patient_id': tmp_bill_patient_id})
        return state

    def cond4(self, state, argv):
        newAppId = argv['Op_Receptionist_makeAppointment_run_8449']['newAppId']
        patientId = argv['Op_Receptionist_makeAppointment_run_8449']['patientId']
        doctorId = argv['Op_Receptionist_makeAppointment_run_8449']['doctorId']
        currentDate = argv['Op_Receptionist_makeAppointment_run_8449']['currentDate']
        day = argv['Op_Receptionist_makeAppointment_run_8449']['day']
        timeSlot = argv['Op_Receptionist_makeAppointment_run_8449']['timeSlot']
        doctor_availability_time_slot = argv['Op_Receptionist_makeAppointment_run_8449']['doctor_availability_time_slot']
        doctor_availability_slmc_reg_no = argv['Op_Receptionist_makeAppointment_run_8449']['doctor_availability_slmc_reg_no']
        doctor_availability_day = argv['Op_Receptionist_makeAppointment_run_8449']['doctor_availability_day']
        tmp_bill_tmp_bill_id = argv['Op_Receptionist_makeAppointment_run_8449']['tmp_bill_tmp_bill_id']
        return And((state['TABLE_appointment'].notNil({'appointment_id': argv['Op_Receptionist_makeAppointment_run_8449']['newAppId']}) == False),(argv['Op_Receptionist_makeAppointment_run_8449']['day'])<=(3631),(state['TABLE_doctor_availability'].notNil({'time_slot': argv['Op_Receptionist_makeAppointment_run_8449']['timeSlot'], 'slmc_reg_no': argv['Op_Receptionist_makeAppointment_run_8449']['doctorId'], 'day': argv['Op_Receptionist_makeAppointment_run_8449']['day']}) == True),(state['TABLE_tmp_bill'].notNil({'patient_id': argv['Op_Receptionist_makeAppointment_run_8449']['patientId']}) == True),(state['TABLE_tmp_bill'].notNil({'tmp_bill_id': state['TABLE_tmp_bill'].get({'patient_id': argv['Op_Receptionist_makeAppointment_run_8449']['patientId']}, 'tmp_bill_id')}) == True))

    def csop4(self, state, argv):
        return True

    def sop4(self, state, argv):
        newAppId = argv['Op_Receptionist_makeAppointment_run_8449']['newAppId']
        patientId = argv['Op_Receptionist_makeAppointment_run_8449']['patientId']
        doctorId = argv['Op_Receptionist_makeAppointment_run_8449']['doctorId']
        currentDate = argv['Op_Receptionist_makeAppointment_run_8449']['currentDate']
        day = argv['Op_Receptionist_makeAppointment_run_8449']['day']
        timeSlot = argv['Op_Receptionist_makeAppointment_run_8449']['timeSlot']
        doctor_availability_time_slot = argv['Op_Receptionist_makeAppointment_run_8449']['doctor_availability_time_slot']
        doctor_availability_slmc_reg_no = argv['Op_Receptionist_makeAppointment_run_8449']['doctor_availability_slmc_reg_no']
        doctor_availability_day = argv['Op_Receptionist_makeAppointment_run_8449']['doctor_availability_day']
        tmp_bill_tmp_bill_id = argv['Op_Receptionist_makeAppointment_run_8449']['tmp_bill_tmp_bill_id']
        appointment_appointment_id = argv['Op_Receptionist_makeAppointment_run_8449']['newAppId']
        appointment_patient_id = argv['Op_Receptionist_makeAppointment_run_8449']['patientId']
        appointment_slmc_reg_no = argv['Op_Receptionist_makeAppointment_run_8449']['doctorId']
        appointment_date = (argv['Op_Receptionist_makeAppointment_run_8449']['currentDate'])+(argv['Op_Receptionist_makeAppointment_run_8449']['day'])
        appointment_cancelled = False
        state['TABLE_appointment'].add({'appointment_id': appointment_appointment_id}, {'patient_id': appointment_patient_id,'slmc_reg_no': appointment_slmc_reg_no,'date': appointment_date,'cancelled': appointment_cancelled})
        doctor_availability_time_slot_id = state['TABLE_doctor_availability'].get({'time_slot': argv['Op_Receptionist_makeAppointment_run_8449']['timeSlot'],'slmc_reg_no': argv['Op_Receptionist_makeAppointment_run_8449']['doctorId'],'day': argv['Op_Receptionist_makeAppointment_run_8449']['day']}, 'time_slot_id')
        doctor_availability_slmc_reg_no = state['TABLE_doctor_availability'].get({'time_slot': argv['Op_Receptionist_makeAppointment_run_8449']['timeSlot'],'slmc_reg_no': argv['Op_Receptionist_makeAppointment_run_8449']['doctorId'],'day': argv['Op_Receptionist_makeAppointment_run_8449']['day']}, 'slmc_reg_no')
        doctor_availability_day = state['TABLE_doctor_availability'].get({'time_slot': argv['Op_Receptionist_makeAppointment_run_8449']['timeSlot'],'slmc_reg_no': argv['Op_Receptionist_makeAppointment_run_8449']['doctorId'],'day': argv['Op_Receptionist_makeAppointment_run_8449']['day']}, 'day')
        doctor_availability_time_slot = state['TABLE_doctor_availability'].get({'time_slot': argv['Op_Receptionist_makeAppointment_run_8449']['timeSlot'],'slmc_reg_no': argv['Op_Receptionist_makeAppointment_run_8449']['doctorId'],'day': argv['Op_Receptionist_makeAppointment_run_8449']['day']}, 'time_slot')
        doctor_availability_current_week_appointments = state['TABLE_doctor_availability'].get({'time_slot': argv['Op_Receptionist_makeAppointment_run_8449']['timeSlot'],'slmc_reg_no': argv['Op_Receptionist_makeAppointment_run_8449']['doctorId'],'day': argv['Op_Receptionist_makeAppointment_run_8449']['day']}, 'current_week_appointments')
        doctor_availability_next_week_appointments = state['TABLE_doctor_availability'].get({'time_slot': argv['Op_Receptionist_makeAppointment_run_8449']['timeSlot'],'slmc_reg_no': argv['Op_Receptionist_makeAppointment_run_8449']['doctorId'],'day': argv['Op_Receptionist_makeAppointment_run_8449']['day']}, 'next_week_appointments')
        doctor_availability_next_week_appointments = (doctor_availability_next_week_appointments)+(1)
        state['TABLE_doctor_availability'].update({'time_slot': argv['Op_Receptionist_makeAppointment_run_8449']['timeSlot'],'slmc_reg_no': argv['Op_Receptionist_makeAppointment_run_8449']['doctorId'],'day': argv['Op_Receptionist_makeAppointment_run_8449']['day']}, {'time_slot_id': doctor_availability_time_slot_id, 'slmc_reg_no': doctor_availability_slmc_reg_no, 'day': doctor_availability_day, 'time_slot': doctor_availability_time_slot, 'current_week_appointments': doctor_availability_current_week_appointments, 'next_week_appointments': doctor_availability_next_week_appointments})
        tmp_bill_tmp_bill_id = state['TABLE_tmp_bill'].get({'tmp_bill_id': state['TABLE_tmp_bill'].get({'patient_id': argv['Op_Receptionist_makeAppointment_run_8449']['patientId']}, 'tmp_bill_id')}, 'tmp_bill_id')
        tmp_bill_doctor_fee = state['TABLE_tmp_bill'].get({'tmp_bill_id': state['TABLE_tmp_bill'].get({'patient_id': argv['Op_Receptionist_makeAppointment_run_8449']['patientId']}, 'tmp_bill_id')}, 'doctor_fee')
        tmp_bill_hospital_fee = state['TABLE_tmp_bill'].get({'tmp_bill_id': state['TABLE_tmp_bill'].get({'patient_id': argv['Op_Receptionist_makeAppointment_run_8449']['patientId']}, 'tmp_bill_id')}, 'hospital_fee')
        tmp_bill_pharmacy_fee = state['TABLE_tmp_bill'].get({'tmp_bill_id': state['TABLE_tmp_bill'].get({'patient_id': argv['Op_Receptionist_makeAppointment_run_8449']['patientId']}, 'tmp_bill_id')}, 'pharmacy_fee')
        tmp_bill_laboratory_fee = state['TABLE_tmp_bill'].get({'tmp_bill_id': state['TABLE_tmp_bill'].get({'patient_id': argv['Op_Receptionist_makeAppointment_run_8449']['patientId']}, 'tmp_bill_id')}, 'laboratory_fee')
        tmp_bill_appointment_fee = state['TABLE_tmp_bill'].get({'tmp_bill_id': state['TABLE_tmp_bill'].get({'patient_id': argv['Op_Receptionist_makeAppointment_run_8449']['patientId']}, 'tmp_bill_id')}, 'appointment_fee')
        tmp_bill_vat = state['TABLE_tmp_bill'].get({'tmp_bill_id': state['TABLE_tmp_bill'].get({'patient_id': argv['Op_Receptionist_makeAppointment_run_8449']['patientId']}, 'tmp_bill_id')}, 'vat')
        tmp_bill_discount = state['TABLE_tmp_bill'].get({'tmp_bill_id': state['TABLE_tmp_bill'].get({'patient_id': argv['Op_Receptionist_makeAppointment_run_8449']['patientId']}, 'tmp_bill_id')}, 'discount')
        tmp_bill_consultant_id = state['TABLE_tmp_bill'].get({'tmp_bill_id': state['TABLE_tmp_bill'].get({'patient_id': argv['Op_Receptionist_makeAppointment_run_8449']['patientId']}, 'tmp_bill_id')}, 'consultant_id')
        tmp_bill_patient_id = state['TABLE_tmp_bill'].get({'tmp_bill_id': state['TABLE_tmp_bill'].get({'patient_id': argv['Op_Receptionist_makeAppointment_run_8449']['patientId']}, 'tmp_bill_id')}, 'patient_id')
        tmp_bill_appointment_fee = 500
        state['TABLE_tmp_bill'].update({'tmp_bill_id': state['TABLE_tmp_bill'].get({'patient_id': argv['Op_Receptionist_makeAppointment_run_8449']['patientId']}, 'tmp_bill_id')}, {'tmp_bill_id': tmp_bill_tmp_bill_id, 'doctor_fee': tmp_bill_doctor_fee, 'hospital_fee': tmp_bill_hospital_fee, 'pharmacy_fee': tmp_bill_pharmacy_fee, 'laboratory_fee': tmp_bill_laboratory_fee, 'appointment_fee': tmp_bill_appointment_fee, 'vat': tmp_bill_vat, 'discount': tmp_bill_discount, 'consultant_id': tmp_bill_consultant_id, 'patient_id': tmp_bill_patient_id})
        return state

    def cond5(self, state, argv):
        newAppId = argv['Op_Receptionist_makeAppointment_run_8449']['newAppId']
        patientId = argv['Op_Receptionist_makeAppointment_run_8449']['patientId']
        doctorId = argv['Op_Receptionist_makeAppointment_run_8449']['doctorId']
        currentDate = argv['Op_Receptionist_makeAppointment_run_8449']['currentDate']
        day = argv['Op_Receptionist_makeAppointment_run_8449']['day']
        timeSlot = argv['Op_Receptionist_makeAppointment_run_8449']['timeSlot']
        doctor_availability_time_slot = argv['Op_Receptionist_makeAppointment_run_8449']['doctor_availability_time_slot']
        doctor_availability_slmc_reg_no = argv['Op_Receptionist_makeAppointment_run_8449']['doctor_availability_slmc_reg_no']
        doctor_availability_day = argv['Op_Receptionist_makeAppointment_run_8449']['doctor_availability_day']
        newTmpBillId = argv['Op_Receptionist_makeAppointment_run_8449']['newTmpBillId']
        return And((state['TABLE_appointment'].notNil({'appointment_id': argv['Op_Receptionist_makeAppointment_run_8449']['newAppId']}) == False),(argv['Op_Receptionist_makeAppointment_run_8449']['day'])<=(3631),(state['TABLE_doctor_availability'].notNil({'time_slot': argv['Op_Receptionist_makeAppointment_run_8449']['timeSlot'], 'slmc_reg_no': argv['Op_Receptionist_makeAppointment_run_8449']['doctorId'], 'day': argv['Op_Receptionist_makeAppointment_run_8449']['day']}) == True),(state['TABLE_tmp_bill'].notNil({'patient_id': argv['Op_Receptionist_makeAppointment_run_8449']['patientId']}) == False))

    def csop5(self, state, argv):
        return True

    def sop5(self, state, argv):
        newAppId = argv['Op_Receptionist_makeAppointment_run_8449']['newAppId']
        patientId = argv['Op_Receptionist_makeAppointment_run_8449']['patientId']
        doctorId = argv['Op_Receptionist_makeAppointment_run_8449']['doctorId']
        currentDate = argv['Op_Receptionist_makeAppointment_run_8449']['currentDate']
        day = argv['Op_Receptionist_makeAppointment_run_8449']['day']
        timeSlot = argv['Op_Receptionist_makeAppointment_run_8449']['timeSlot']
        doctor_availability_time_slot = argv['Op_Receptionist_makeAppointment_run_8449']['doctor_availability_time_slot']
        doctor_availability_slmc_reg_no = argv['Op_Receptionist_makeAppointment_run_8449']['doctor_availability_slmc_reg_no']
        doctor_availability_day = argv['Op_Receptionist_makeAppointment_run_8449']['doctor_availability_day']
        newTmpBillId = argv['Op_Receptionist_makeAppointment_run_8449']['newTmpBillId']
        appointment_appointment_id = argv['Op_Receptionist_makeAppointment_run_8449']['newAppId']
        appointment_patient_id = argv['Op_Receptionist_makeAppointment_run_8449']['patientId']
        appointment_slmc_reg_no = argv['Op_Receptionist_makeAppointment_run_8449']['doctorId']
        appointment_date = (argv['Op_Receptionist_makeAppointment_run_8449']['currentDate'])+(argv['Op_Receptionist_makeAppointment_run_8449']['day'])
        appointment_cancelled = False
        state['TABLE_appointment'].add({'appointment_id': appointment_appointment_id}, {'patient_id': appointment_patient_id,'slmc_reg_no': appointment_slmc_reg_no,'date': appointment_date,'cancelled': appointment_cancelled})
        doctor_availability_time_slot_id = state['TABLE_doctor_availability'].get({'time_slot': argv['Op_Receptionist_makeAppointment_run_8449']['timeSlot'],'slmc_reg_no': argv['Op_Receptionist_makeAppointment_run_8449']['doctorId'],'day': argv['Op_Receptionist_makeAppointment_run_8449']['day']}, 'time_slot_id')
        doctor_availability_slmc_reg_no = state['TABLE_doctor_availability'].get({'time_slot': argv['Op_Receptionist_makeAppointment_run_8449']['timeSlot'],'slmc_reg_no': argv['Op_Receptionist_makeAppointment_run_8449']['doctorId'],'day': argv['Op_Receptionist_makeAppointment_run_8449']['day']}, 'slmc_reg_no')
        doctor_availability_day = state['TABLE_doctor_availability'].get({'time_slot': argv['Op_Receptionist_makeAppointment_run_8449']['timeSlot'],'slmc_reg_no': argv['Op_Receptionist_makeAppointment_run_8449']['doctorId'],'day': argv['Op_Receptionist_makeAppointment_run_8449']['day']}, 'day')
        doctor_availability_time_slot = state['TABLE_doctor_availability'].get({'time_slot': argv['Op_Receptionist_makeAppointment_run_8449']['timeSlot'],'slmc_reg_no': argv['Op_Receptionist_makeAppointment_run_8449']['doctorId'],'day': argv['Op_Receptionist_makeAppointment_run_8449']['day']}, 'time_slot')
        doctor_availability_current_week_appointments = state['TABLE_doctor_availability'].get({'time_slot': argv['Op_Receptionist_makeAppointment_run_8449']['timeSlot'],'slmc_reg_no': argv['Op_Receptionist_makeAppointment_run_8449']['doctorId'],'day': argv['Op_Receptionist_makeAppointment_run_8449']['day']}, 'current_week_appointments')
        doctor_availability_next_week_appointments = state['TABLE_doctor_availability'].get({'time_slot': argv['Op_Receptionist_makeAppointment_run_8449']['timeSlot'],'slmc_reg_no': argv['Op_Receptionist_makeAppointment_run_8449']['doctorId'],'day': argv['Op_Receptionist_makeAppointment_run_8449']['day']}, 'next_week_appointments')
        doctor_availability_current_week_appointments = (doctor_availability_current_week_appointments)+(1)
        state['TABLE_doctor_availability'].update({'time_slot': argv['Op_Receptionist_makeAppointment_run_8449']['timeSlot'],'slmc_reg_no': argv['Op_Receptionist_makeAppointment_run_8449']['doctorId'],'day': argv['Op_Receptionist_makeAppointment_run_8449']['day']}, {'time_slot_id': doctor_availability_time_slot_id, 'slmc_reg_no': doctor_availability_slmc_reg_no, 'day': doctor_availability_day, 'time_slot': doctor_availability_time_slot, 'current_week_appointments': doctor_availability_current_week_appointments, 'next_week_appointments': doctor_availability_next_week_appointments})
        tmp_bill_patient_id = argv['Op_Receptionist_makeAppointment_run_8449']['patientId']
        tmp_bill_appointment_fee = 500
        tmp_bill_tmp_bill_id = argv['Op_Receptionist_makeAppointment_run_8449']['newTmpBillId']
        state['TABLE_tmp_bill'].add({'tmp_bill_id': tmp_bill_tmp_bill_id}, {'patient_id': tmp_bill_patient_id,'appointment_fee': tmp_bill_appointment_fee})
        return state

    def cond6(self, state, argv):
        newAppId = argv['Op_Receptionist_makeAppointment_run_8449']['newAppId']
        patientId = argv['Op_Receptionist_makeAppointment_run_8449']['patientId']
        doctorId = argv['Op_Receptionist_makeAppointment_run_8449']['doctorId']
        currentDate = argv['Op_Receptionist_makeAppointment_run_8449']['currentDate']
        day = argv['Op_Receptionist_makeAppointment_run_8449']['day']
        timeSlot = argv['Op_Receptionist_makeAppointment_run_8449']['timeSlot']
        doctor_availability_time_slot = argv['Op_Receptionist_makeAppointment_run_8449']['doctor_availability_time_slot']
        doctor_availability_slmc_reg_no = argv['Op_Receptionist_makeAppointment_run_8449']['doctor_availability_slmc_reg_no']
        doctor_availability_day = argv['Op_Receptionist_makeAppointment_run_8449']['doctor_availability_day']
        newTmpBillId = argv['Op_Receptionist_makeAppointment_run_8449']['newTmpBillId']
        return And((state['TABLE_appointment'].notNil({'appointment_id': argv['Op_Receptionist_makeAppointment_run_8449']['newAppId']}) == False),(argv['Op_Receptionist_makeAppointment_run_8449']['day'])<=(3631),(state['TABLE_doctor_availability'].notNil({'time_slot': argv['Op_Receptionist_makeAppointment_run_8449']['timeSlot'], 'slmc_reg_no': argv['Op_Receptionist_makeAppointment_run_8449']['doctorId'], 'day': argv['Op_Receptionist_makeAppointment_run_8449']['day']}) == True),(state['TABLE_tmp_bill'].notNil({'patient_id': argv['Op_Receptionist_makeAppointment_run_8449']['patientId']}) == False))

    def csop6(self, state, argv):
        return True

    def sop6(self, state, argv):
        newAppId = argv['Op_Receptionist_makeAppointment_run_8449']['newAppId']
        patientId = argv['Op_Receptionist_makeAppointment_run_8449']['patientId']
        doctorId = argv['Op_Receptionist_makeAppointment_run_8449']['doctorId']
        currentDate = argv['Op_Receptionist_makeAppointment_run_8449']['currentDate']
        day = argv['Op_Receptionist_makeAppointment_run_8449']['day']
        timeSlot = argv['Op_Receptionist_makeAppointment_run_8449']['timeSlot']
        doctor_availability_time_slot = argv['Op_Receptionist_makeAppointment_run_8449']['doctor_availability_time_slot']
        doctor_availability_slmc_reg_no = argv['Op_Receptionist_makeAppointment_run_8449']['doctor_availability_slmc_reg_no']
        doctor_availability_day = argv['Op_Receptionist_makeAppointment_run_8449']['doctor_availability_day']
        newTmpBillId = argv['Op_Receptionist_makeAppointment_run_8449']['newTmpBillId']
        appointment_appointment_id = argv['Op_Receptionist_makeAppointment_run_8449']['newAppId']
        appointment_patient_id = argv['Op_Receptionist_makeAppointment_run_8449']['patientId']
        appointment_slmc_reg_no = argv['Op_Receptionist_makeAppointment_run_8449']['doctorId']
        appointment_date = (argv['Op_Receptionist_makeAppointment_run_8449']['currentDate'])+(argv['Op_Receptionist_makeAppointment_run_8449']['day'])
        appointment_cancelled = False
        state['TABLE_appointment'].add({'appointment_id': appointment_appointment_id}, {'patient_id': appointment_patient_id,'slmc_reg_no': appointment_slmc_reg_no,'date': appointment_date,'cancelled': appointment_cancelled})
        doctor_availability_time_slot_id = state['TABLE_doctor_availability'].get({'time_slot': argv['Op_Receptionist_makeAppointment_run_8449']['timeSlot'],'slmc_reg_no': argv['Op_Receptionist_makeAppointment_run_8449']['doctorId'],'day': argv['Op_Receptionist_makeAppointment_run_8449']['day']}, 'time_slot_id')
        doctor_availability_slmc_reg_no = state['TABLE_doctor_availability'].get({'time_slot': argv['Op_Receptionist_makeAppointment_run_8449']['timeSlot'],'slmc_reg_no': argv['Op_Receptionist_makeAppointment_run_8449']['doctorId'],'day': argv['Op_Receptionist_makeAppointment_run_8449']['day']}, 'slmc_reg_no')
        doctor_availability_day = state['TABLE_doctor_availability'].get({'time_slot': argv['Op_Receptionist_makeAppointment_run_8449']['timeSlot'],'slmc_reg_no': argv['Op_Receptionist_makeAppointment_run_8449']['doctorId'],'day': argv['Op_Receptionist_makeAppointment_run_8449']['day']}, 'day')
        doctor_availability_time_slot = state['TABLE_doctor_availability'].get({'time_slot': argv['Op_Receptionist_makeAppointment_run_8449']['timeSlot'],'slmc_reg_no': argv['Op_Receptionist_makeAppointment_run_8449']['doctorId'],'day': argv['Op_Receptionist_makeAppointment_run_8449']['day']}, 'time_slot')
        doctor_availability_current_week_appointments = state['TABLE_doctor_availability'].get({'time_slot': argv['Op_Receptionist_makeAppointment_run_8449']['timeSlot'],'slmc_reg_no': argv['Op_Receptionist_makeAppointment_run_8449']['doctorId'],'day': argv['Op_Receptionist_makeAppointment_run_8449']['day']}, 'current_week_appointments')
        doctor_availability_next_week_appointments = state['TABLE_doctor_availability'].get({'time_slot': argv['Op_Receptionist_makeAppointment_run_8449']['timeSlot'],'slmc_reg_no': argv['Op_Receptionist_makeAppointment_run_8449']['doctorId'],'day': argv['Op_Receptionist_makeAppointment_run_8449']['day']}, 'next_week_appointments')
        doctor_availability_next_week_appointments = (doctor_availability_next_week_appointments)+(1)
        state['TABLE_doctor_availability'].update({'time_slot': argv['Op_Receptionist_makeAppointment_run_8449']['timeSlot'],'slmc_reg_no': argv['Op_Receptionist_makeAppointment_run_8449']['doctorId'],'day': argv['Op_Receptionist_makeAppointment_run_8449']['day']}, {'time_slot_id': doctor_availability_time_slot_id, 'slmc_reg_no': doctor_availability_slmc_reg_no, 'day': doctor_availability_day, 'time_slot': doctor_availability_time_slot, 'current_week_appointments': doctor_availability_current_week_appointments, 'next_week_appointments': doctor_availability_next_week_appointments})
        tmp_bill_patient_id = argv['Op_Receptionist_makeAppointment_run_8449']['patientId']
        tmp_bill_appointment_fee = 500
        tmp_bill_tmp_bill_id = argv['Op_Receptionist_makeAppointment_run_8449']['newTmpBillId']
        state['TABLE_tmp_bill'].add({'tmp_bill_id': tmp_bill_tmp_bill_id}, {'patient_id': tmp_bill_patient_id,'appointment_fee': tmp_bill_appointment_fee})
        return state


class Op_Pharmacist_addNewSupplier_run_8450():
    def __init__(self):
        self.sops = [(self.cond0, self.csop0, self.sop0)]
        self.axiom = AxiomEmpty()

    def cond0(self, state, argv):
        newSupplierId = argv['Op_Pharmacist_addNewSupplier_run_8450']['newSupplierId']
        name = argv['Op_Pharmacist_addNewSupplier_run_8450']['name']
        return (state['TABLE_suppliers'].notNil({'supplier_id': argv['Op_Pharmacist_addNewSupplier_run_8450']['newSupplierId']}) == False)

    def csop0(self, state, argv):
        return True

    def sop0(self, state, argv):
        newSupplierId = argv['Op_Pharmacist_addNewSupplier_run_8450']['newSupplierId']
        name = argv['Op_Pharmacist_addNewSupplier_run_8450']['name']
        suppliers_supplier_id = argv['Op_Pharmacist_addNewSupplier_run_8450']['newSupplierId']
        suppliers_supplier_name = argv['Op_Pharmacist_addNewSupplier_run_8450']['name']
        state['TABLE_suppliers'].add({'supplier_id': suppliers_supplier_id}, {'supplier_name': suppliers_supplier_name})
        return state


class Op_Pharmacist_updatePharmacistInfo_run_8451():
    def __init__(self):
        self.sops = [(self.cond0, self.csop0, self.sop0)]
        self.axiom = AxiomEmpty()

    def cond0(self, state, argv):
        id = argv['Op_Pharmacist_updatePharmacistInfo_run_8451']['id']
        pharmacist_pharmacist_id = argv['Op_Pharmacist_updatePharmacistInfo_run_8451']['pharmacist_pharmacist_id']
        return (state['TABLE_pharmacist'].notNil({'pharmacist_id': argv['Op_Pharmacist_updatePharmacistInfo_run_8451']['id']}) == True)

    def csop0(self, state, argv):
        return True

    def sop0(self, state, argv):
        id = argv['Op_Pharmacist_updatePharmacistInfo_run_8451']['id']
        pharmacist_pharmacist_id = argv['Op_Pharmacist_updatePharmacistInfo_run_8451']['pharmacist_pharmacist_id']
        pharmacist_pharmacist_id = state['TABLE_pharmacist'].get({'pharmacist_id': argv['Op_Pharmacist_updatePharmacistInfo_run_8451']['id']}, 'pharmacist_id')
        pharmacist_user_id = state['TABLE_pharmacist'].get({'pharmacist_id': argv['Op_Pharmacist_updatePharmacistInfo_run_8451']['id']}, 'user_id')
        pharmacist_education = state['TABLE_pharmacist'].get({'pharmacist_id': argv['Op_Pharmacist_updatePharmacistInfo_run_8451']['id']}, 'education')
        pharmacist_training = state['TABLE_pharmacist'].get({'pharmacist_id': argv['Op_Pharmacist_updatePharmacistInfo_run_8451']['id']}, 'training')
        pharmacist_experience = state['TABLE_pharmacist'].get({'pharmacist_id': argv['Op_Pharmacist_updatePharmacistInfo_run_8451']['id']}, 'experience')
        pharmacist_achievements = state['TABLE_pharmacist'].get({'pharmacist_id': argv['Op_Pharmacist_updatePharmacistInfo_run_8451']['id']}, 'achievements')
        pharmacist_education = argv['Op_Pharmacist_updatePharmacistInfo_run_8451']['id']
        state['TABLE_pharmacist'].update({'pharmacist_id': argv['Op_Pharmacist_updatePharmacistInfo_run_8451']['id']}, {'pharmacist_id': pharmacist_pharmacist_id, 'user_id': pharmacist_user_id, 'education': pharmacist_education, 'training': pharmacist_training, 'experience': pharmacist_experience, 'achievements': pharmacist_achievements})
        return state


class Op_LabAssistant_updateProfileInfo_run_8452():
    def __init__(self):
        self.sops = [(self.cond0, self.csop0, self.sop0)]
        self.axiom = AxiomEmpty()

    def cond0(self, state, argv):
        id = argv['Op_LabAssistant_updateProfileInfo_run_8452']['id']
        sys_user_person_id = argv['Op_LabAssistant_updateProfileInfo_run_8452']['sys_user_person_id']
        person_person_id = argv['Op_LabAssistant_updateProfileInfo_run_8452']['person_person_id']
        return And((state['TABLE_sys_user'].notNil({'user_id': argv['Op_LabAssistant_updateProfileInfo_run_8452']['id']}) == True),(state['TABLE_person'].notNil({'person_id': state['TABLE_sys_user'].get({'user_id': argv['Op_LabAssistant_updateProfileInfo_run_8452']['id']}, 'person_id')}) == True))

    def csop0(self, state, argv):
        return True

    def sop0(self, state, argv):
        id = argv['Op_LabAssistant_updateProfileInfo_run_8452']['id']
        sys_user_person_id = argv['Op_LabAssistant_updateProfileInfo_run_8452']['sys_user_person_id']
        person_person_id = argv['Op_LabAssistant_updateProfileInfo_run_8452']['person_person_id']
        person_person_id = state['TABLE_person'].get({'person_id': state['TABLE_sys_user'].get({'user_id': argv['Op_LabAssistant_updateProfileInfo_run_8452']['id']}, 'person_id')}, 'person_id')
        person_user_id = state['TABLE_person'].get({'person_id': state['TABLE_sys_user'].get({'user_id': argv['Op_LabAssistant_updateProfileInfo_run_8452']['id']}, 'person_id')}, 'user_id')
        person_nic = state['TABLE_person'].get({'person_id': state['TABLE_sys_user'].get({'user_id': argv['Op_LabAssistant_updateProfileInfo_run_8452']['id']}, 'person_id')}, 'nic')
        person_gender = state['TABLE_person'].get({'person_id': state['TABLE_sys_user'].get({'user_id': argv['Op_LabAssistant_updateProfileInfo_run_8452']['id']}, 'person_id')}, 'gender')
        person_date_of_birth = state['TABLE_person'].get({'person_id': state['TABLE_sys_user'].get({'user_id': argv['Op_LabAssistant_updateProfileInfo_run_8452']['id']}, 'person_id')}, 'date_of_birth')
        person_address = state['TABLE_person'].get({'person_id': state['TABLE_sys_user'].get({'user_id': argv['Op_LabAssistant_updateProfileInfo_run_8452']['id']}, 'person_id')}, 'address')
        person_mobile = state['TABLE_person'].get({'person_id': state['TABLE_sys_user'].get({'user_id': argv['Op_LabAssistant_updateProfileInfo_run_8452']['id']}, 'person_id')}, 'mobile')
        person_first_name = state['TABLE_person'].get({'person_id': state['TABLE_sys_user'].get({'user_id': argv['Op_LabAssistant_updateProfileInfo_run_8452']['id']}, 'person_id')}, 'first_name')
        person_last_name = state['TABLE_person'].get({'person_id': state['TABLE_sys_user'].get({'user_id': argv['Op_LabAssistant_updateProfileInfo_run_8452']['id']}, 'person_id')}, 'last_name')
        person_email = state['TABLE_person'].get({'person_id': state['TABLE_sys_user'].get({'user_id': argv['Op_LabAssistant_updateProfileInfo_run_8452']['id']}, 'person_id')}, 'email')
        person_nationality = state['TABLE_person'].get({'person_id': state['TABLE_sys_user'].get({'user_id': argv['Op_LabAssistant_updateProfileInfo_run_8452']['id']}, 'person_id')}, 'nationality')
        person_religion = state['TABLE_person'].get({'person_id': state['TABLE_sys_user'].get({'user_id': argv['Op_LabAssistant_updateProfileInfo_run_8452']['id']}, 'person_id')}, 'religion')
        person_address = argv['Op_LabAssistant_updateProfileInfo_run_8452']['id']
        state['TABLE_person'].update({'person_id': state['TABLE_sys_user'].get({'user_id': argv['Op_LabAssistant_updateProfileInfo_run_8452']['id']}, 'person_id')}, {'person_id': person_person_id, 'user_id': person_user_id, 'nic': person_nic, 'gender': person_gender, 'date_of_birth': person_date_of_birth, 'address': person_address, 'mobile': person_mobile, 'first_name': person_first_name, 'last_name': person_last_name, 'email': person_email, 'nationality': person_nationality, 'religion': person_religion})
        return state


class Op_Cashier_removeFromTempBill_run_8453():
    def __init__(self):
        self.sops = [(self.cond0, self.csop0, self.sop0)]
        self.axiom = AxiomEmpty()

    def cond0(self, state, argv):
        id = argv['Op_Cashier_removeFromTempBill_run_8453']['id']
        return True

    def csop0(self, state, argv):
        return True

    def sop0(self, state, argv):
        id = argv['Op_Cashier_removeFromTempBill_run_8453']['id']
        state['TABLE_tmp_bill'].delete({'patient_id': argv['Op_Cashier_removeFromTempBill_run_8453']['id']})
        return state


class Op_LabAssistant_liverFunctionTest_run_8454():
    def __init__(self):
        self.sops = [(self.cond0, self.csop0, self.sop0)]
        self.axiom = AxiomEmpty()

    def cond0(self, state, argv):
        newTstId = argv['Op_LabAssistant_liverFunctionTest_run_8454']['newTstId']
        appId = argv['Op_LabAssistant_liverFunctionTest_run_8454']['appId']
        totalBilirubin = argv['Op_LabAssistant_liverFunctionTest_run_8454']['totalBilirubin']
        albumin = argv['Op_LabAssistant_liverFunctionTest_run_8454']['albumin']
        globulin = argv['Op_LabAssistant_liverFunctionTest_run_8454']['globulin']
        directBilirubin = argv['Op_LabAssistant_liverFunctionTest_run_8454']['directBilirubin']
        sgotast = argv['Op_LabAssistant_liverFunctionTest_run_8454']['sgotast']
        sgptalt = argv['Op_LabAssistant_liverFunctionTest_run_8454']['sgptalt']
        alkalinePhospates = argv['Op_LabAssistant_liverFunctionTest_run_8454']['alkalinePhospates']
        now = argv['Op_LabAssistant_liverFunctionTest_run_8454']['now']
        return (state['TABLE_LiverFunctionTest'].notNil({'tst_liver_id': argv['Op_LabAssistant_liverFunctionTest_run_8454']['newTstId']}) == False)

    def csop0(self, state, argv):
        return True

    def sop0(self, state, argv):
        newTstId = argv['Op_LabAssistant_liverFunctionTest_run_8454']['newTstId']
        appId = argv['Op_LabAssistant_liverFunctionTest_run_8454']['appId']
        totalBilirubin = argv['Op_LabAssistant_liverFunctionTest_run_8454']['totalBilirubin']
        albumin = argv['Op_LabAssistant_liverFunctionTest_run_8454']['albumin']
        globulin = argv['Op_LabAssistant_liverFunctionTest_run_8454']['globulin']
        directBilirubin = argv['Op_LabAssistant_liverFunctionTest_run_8454']['directBilirubin']
        sgotast = argv['Op_LabAssistant_liverFunctionTest_run_8454']['sgotast']
        sgptalt = argv['Op_LabAssistant_liverFunctionTest_run_8454']['sgptalt']
        alkalinePhospates = argv['Op_LabAssistant_liverFunctionTest_run_8454']['alkalinePhospates']
        now = argv['Op_LabAssistant_liverFunctionTest_run_8454']['now']
        LiverFunctionTest_tst_liver_id = argv['Op_LabAssistant_liverFunctionTest_run_8454']['newTstId']
        LiverFunctionTest_appointment_id = argv['Op_LabAssistant_liverFunctionTest_run_8454']['appId']
        LiverFunctionTest_totalProtein = argv['Op_LabAssistant_liverFunctionTest_run_8454']['totalBilirubin']
        LiverFunctionTest_albumin = argv['Op_LabAssistant_liverFunctionTest_run_8454']['albumin']
        LiverFunctionTest_globulin = argv['Op_LabAssistant_liverFunctionTest_run_8454']['globulin']
        LiverFunctionTest_totalBilirubin = argv['Op_LabAssistant_liverFunctionTest_run_8454']['totalBilirubin']
        LiverFunctionTest_directBilirubin = argv['Op_LabAssistant_liverFunctionTest_run_8454']['directBilirubin']
        LiverFunctionTest_sgotast = argv['Op_LabAssistant_liverFunctionTest_run_8454']['sgotast']
        LiverFunctionTest_sgptalt = argv['Op_LabAssistant_liverFunctionTest_run_8454']['sgptalt']
        LiverFunctionTest_alkalinePhospates = argv['Op_LabAssistant_liverFunctionTest_run_8454']['alkalinePhospates']
        LiverFunctionTest_date = argv['Op_LabAssistant_liverFunctionTest_run_8454']['now']
        state['TABLE_LiverFunctionTest'].add({'tst_liver_id': LiverFunctionTest_tst_liver_id}, {'appointment_id': LiverFunctionTest_appointment_id,'totalProtein': LiverFunctionTest_totalProtein,'albumin': LiverFunctionTest_albumin,'globulin': LiverFunctionTest_globulin,'totalBilirubin': LiverFunctionTest_totalBilirubin,'directBilirubin': LiverFunctionTest_directBilirubin,'sgotast': LiverFunctionTest_sgotast,'sgptalt': LiverFunctionTest_sgptalt,'alkalinePhospates': LiverFunctionTest_alkalinePhospates,'date': LiverFunctionTest_date})
        return state


class Op_Receptionist_cancelLabAppointment_run_8455():
    def __init__(self):
        self.sops = [(self.cond0, self.csop0, self.sop0), (self.cond1, self.csop1, self.sop1), (self.cond2, self.csop2, self.sop2)]
        self.axiom = AxiomEmpty()

    def cond0(self, state, argv):
        labAppointmentId = argv['Op_Receptionist_cancelLabAppointment_run_8455']['labAppointmentId']
        lab_appointment_lab_appointment_id = argv['Op_Receptionist_cancelLabAppointment_run_8455']['lab_appointment_lab_appointment_id']
        labAppointmentId = argv['Op_Receptionist_cancelLabAppointment_run_8455']['labAppointmentId']
        lab_appointment_lab_appointment_id = argv['Op_Receptionist_cancelLabAppointment_run_8455']['lab_appointment_lab_appointment_id']
        lab_appointment_bill_id = argv['Op_Receptionist_cancelLabAppointment_run_8455']['lab_appointment_bill_id']
        newRefundId = argv['Op_Receptionist_cancelLabAppointment_run_8455']['newRefundId']
        bill_total = argv['Op_Receptionist_cancelLabAppointment_run_8455']['bill_total']
        now = argv['Op_Receptionist_cancelLabAppointment_run_8455']['now']
        labAppointmentId = argv['Op_Receptionist_cancelLabAppointment_run_8455']['labAppointmentId']
        lab_appointment_lab_appointment_id = argv['Op_Receptionist_cancelLabAppointment_run_8455']['lab_appointment_lab_appointment_id']
        lab_appointment_bill_id = argv['Op_Receptionist_cancelLabAppointment_run_8455']['lab_appointment_bill_id']
        newRefundId = argv['Op_Receptionist_cancelLabAppointment_run_8455']['newRefundId']
        bill_total = argv['Op_Receptionist_cancelLabAppointment_run_8455']['bill_total']
        now = argv['Op_Receptionist_cancelLabAppointment_run_8455']['now']
        bill_bill_id = argv['Op_Receptionist_cancelLabAppointment_run_8455']['bill_bill_id']
        return And((state['TABLE_lab_appointment'].notNil({'lab_appointment_id': argv['Op_Receptionist_cancelLabAppointment_run_8455']['labAppointmentId']}) == True),Not((state['TABLE_lab_appointment'].notNil({'lab_appointment_id': argv['Op_Receptionist_cancelLabAppointment_run_8455']['labAppointmentId']}) == True)),Not((state['TABLE_lab_appointment'].notNil({'lab_appointment_id': argv['Op_Receptionist_cancelLabAppointment_run_8455']['labAppointmentId']}) == True)),Not((state['TABLE_bill'].notNil({'bill_id': state['TABLE_lab_appointment'].get({'lab_appointment_id': argv['Op_Receptionist_cancelLabAppointment_run_8455']['labAppointmentId']}, 'bill_id')}) == True)),Not((state['TABLE_lab_appointment'].notNil({'lab_appointment_id': argv['Op_Receptionist_cancelLabAppointment_run_8455']['labAppointmentId']}) == True)),Not((state['TABLE_lab_appointment'].notNil({'lab_appointment_id': argv['Op_Receptionist_cancelLabAppointment_run_8455']['labAppointmentId']}) == True)),Not((state['TABLE_bill'].notNil({'bill_id': state['TABLE_lab_appointment'].get({'lab_appointment_id': argv['Op_Receptionist_cancelLabAppointment_run_8455']['labAppointmentId']}, 'bill_id')}) == True)),Not((state['TABLE_bill'].notNil({'bill_id': state['TABLE_lab_appointment'].get({'lab_appointment_id': argv['Op_Receptionist_cancelLabAppointment_run_8455']['labAppointmentId']}, 'bill_id')}) == True)))

    def csop0(self, state, argv):
        return True

    def sop0(self, state, argv):
        labAppointmentId = argv['Op_Receptionist_cancelLabAppointment_run_8455']['labAppointmentId']
        lab_appointment_lab_appointment_id = argv['Op_Receptionist_cancelLabAppointment_run_8455']['lab_appointment_lab_appointment_id']
        lab_appointment_lab_appointment_id = state['TABLE_lab_appointment'].get({'lab_appointment_id': argv['Op_Receptionist_cancelLabAppointment_run_8455']['labAppointmentId']}, 'lab_appointment_id')
        lab_appointment_test_id = state['TABLE_lab_appointment'].get({'lab_appointment_id': argv['Op_Receptionist_cancelLabAppointment_run_8455']['labAppointmentId']}, 'test_id')
        lab_appointment_date = state['TABLE_lab_appointment'].get({'lab_appointment_id': argv['Op_Receptionist_cancelLabAppointment_run_8455']['labAppointmentId']}, 'date')
        lab_appointment_info = state['TABLE_lab_appointment'].get({'lab_appointment_id': argv['Op_Receptionist_cancelLabAppointment_run_8455']['labAppointmentId']}, 'info')
        lab_appointment_patient_id = state['TABLE_lab_appointment'].get({'lab_appointment_id': argv['Op_Receptionist_cancelLabAppointment_run_8455']['labAppointmentId']}, 'patient_id')
        lab_appointment_bill_id = state['TABLE_lab_appointment'].get({'lab_appointment_id': argv['Op_Receptionist_cancelLabAppointment_run_8455']['labAppointmentId']}, 'bill_id')
        lab_appointment_lab_assistant_id = state['TABLE_lab_appointment'].get({'lab_appointment_id': argv['Op_Receptionist_cancelLabAppointment_run_8455']['labAppointmentId']}, 'lab_assistant_id')
        lab_appointment_cancelled = state['TABLE_lab_appointment'].get({'lab_appointment_id': argv['Op_Receptionist_cancelLabAppointment_run_8455']['labAppointmentId']}, 'cancelled')
        lab_appointment_doctor_id = state['TABLE_lab_appointment'].get({'lab_appointment_id': argv['Op_Receptionist_cancelLabAppointment_run_8455']['labAppointmentId']}, 'doctor_id')
        lab_appointment_cancelled = True
        state['TABLE_lab_appointment'].update({'lab_appointment_id': argv['Op_Receptionist_cancelLabAppointment_run_8455']['labAppointmentId']}, {'lab_appointment_id': lab_appointment_lab_appointment_id, 'test_id': lab_appointment_test_id, 'date': lab_appointment_date, 'info': lab_appointment_info, 'patient_id': lab_appointment_patient_id, 'bill_id': lab_appointment_bill_id, 'lab_assistant_id': lab_appointment_lab_assistant_id, 'cancelled': lab_appointment_cancelled, 'doctor_id': lab_appointment_doctor_id})
        return state

    def cond1(self, state, argv):
        labAppointmentId = argv['Op_Receptionist_cancelLabAppointment_run_8455']['labAppointmentId']
        lab_appointment_lab_appointment_id = argv['Op_Receptionist_cancelLabAppointment_run_8455']['lab_appointment_lab_appointment_id']
        lab_appointment_bill_id = argv['Op_Receptionist_cancelLabAppointment_run_8455']['lab_appointment_bill_id']
        newRefundId = argv['Op_Receptionist_cancelLabAppointment_run_8455']['newRefundId']
        bill_total = argv['Op_Receptionist_cancelLabAppointment_run_8455']['bill_total']
        now = argv['Op_Receptionist_cancelLabAppointment_run_8455']['now']
        labAppointmentId = argv['Op_Receptionist_cancelLabAppointment_run_8455']['labAppointmentId']
        lab_appointment_lab_appointment_id = argv['Op_Receptionist_cancelLabAppointment_run_8455']['lab_appointment_lab_appointment_id']
        lab_appointment_bill_id = argv['Op_Receptionist_cancelLabAppointment_run_8455']['lab_appointment_bill_id']
        newRefundId = argv['Op_Receptionist_cancelLabAppointment_run_8455']['newRefundId']
        bill_total = argv['Op_Receptionist_cancelLabAppointment_run_8455']['bill_total']
        now = argv['Op_Receptionist_cancelLabAppointment_run_8455']['now']
        bill_bill_id = argv['Op_Receptionist_cancelLabAppointment_run_8455']['bill_bill_id']
        return And((state['TABLE_lab_appointment'].notNil({'lab_appointment_id': argv['Op_Receptionist_cancelLabAppointment_run_8455']['labAppointmentId']}) == True),(state['TABLE_lab_appointment'].notNil({'lab_appointment_id': argv['Op_Receptionist_cancelLabAppointment_run_8455']['labAppointmentId']}) == True),(state['TABLE_bill'].notNil({'bill_id': state['TABLE_lab_appointment'].get({'lab_appointment_id': argv['Op_Receptionist_cancelLabAppointment_run_8455']['labAppointmentId']}, 'bill_id')}) == True),Not((state['TABLE_lab_appointment'].notNil({'lab_appointment_id': argv['Op_Receptionist_cancelLabAppointment_run_8455']['labAppointmentId']}) == True)),Not((state['TABLE_lab_appointment'].notNil({'lab_appointment_id': argv['Op_Receptionist_cancelLabAppointment_run_8455']['labAppointmentId']}) == True)),Not((state['TABLE_bill'].notNil({'bill_id': state['TABLE_lab_appointment'].get({'lab_appointment_id': argv['Op_Receptionist_cancelLabAppointment_run_8455']['labAppointmentId']}, 'bill_id')}) == True)),Not((state['TABLE_bill'].notNil({'bill_id': state['TABLE_lab_appointment'].get({'lab_appointment_id': argv['Op_Receptionist_cancelLabAppointment_run_8455']['labAppointmentId']}, 'bill_id')}) == True)))

    def csop1(self, state, argv):
        return True

    def sop1(self, state, argv):
        labAppointmentId = argv['Op_Receptionist_cancelLabAppointment_run_8455']['labAppointmentId']
        lab_appointment_lab_appointment_id = argv['Op_Receptionist_cancelLabAppointment_run_8455']['lab_appointment_lab_appointment_id']
        lab_appointment_bill_id = argv['Op_Receptionist_cancelLabAppointment_run_8455']['lab_appointment_bill_id']
        newRefundId = argv['Op_Receptionist_cancelLabAppointment_run_8455']['newRefundId']
        bill_total = argv['Op_Receptionist_cancelLabAppointment_run_8455']['bill_total']
        now = argv['Op_Receptionist_cancelLabAppointment_run_8455']['now']
        lab_appointment_lab_appointment_id = state['TABLE_lab_appointment'].get({'lab_appointment_id': argv['Op_Receptionist_cancelLabAppointment_run_8455']['labAppointmentId']}, 'lab_appointment_id')
        lab_appointment_test_id = state['TABLE_lab_appointment'].get({'lab_appointment_id': argv['Op_Receptionist_cancelLabAppointment_run_8455']['labAppointmentId']}, 'test_id')
        lab_appointment_date = state['TABLE_lab_appointment'].get({'lab_appointment_id': argv['Op_Receptionist_cancelLabAppointment_run_8455']['labAppointmentId']}, 'date')
        lab_appointment_info = state['TABLE_lab_appointment'].get({'lab_appointment_id': argv['Op_Receptionist_cancelLabAppointment_run_8455']['labAppointmentId']}, 'info')
        lab_appointment_patient_id = state['TABLE_lab_appointment'].get({'lab_appointment_id': argv['Op_Receptionist_cancelLabAppointment_run_8455']['labAppointmentId']}, 'patient_id')
        lab_appointment_bill_id = state['TABLE_lab_appointment'].get({'lab_appointment_id': argv['Op_Receptionist_cancelLabAppointment_run_8455']['labAppointmentId']}, 'bill_id')
        lab_appointment_lab_assistant_id = state['TABLE_lab_appointment'].get({'lab_appointment_id': argv['Op_Receptionist_cancelLabAppointment_run_8455']['labAppointmentId']}, 'lab_assistant_id')
        lab_appointment_cancelled = state['TABLE_lab_appointment'].get({'lab_appointment_id': argv['Op_Receptionist_cancelLabAppointment_run_8455']['labAppointmentId']}, 'cancelled')
        lab_appointment_doctor_id = state['TABLE_lab_appointment'].get({'lab_appointment_id': argv['Op_Receptionist_cancelLabAppointment_run_8455']['labAppointmentId']}, 'doctor_id')
        lab_appointment_cancelled = True
        state['TABLE_lab_appointment'].update({'lab_appointment_id': argv['Op_Receptionist_cancelLabAppointment_run_8455']['labAppointmentId']}, {'lab_appointment_id': lab_appointment_lab_appointment_id, 'test_id': lab_appointment_test_id, 'date': lab_appointment_date, 'info': lab_appointment_info, 'patient_id': lab_appointment_patient_id, 'bill_id': lab_appointment_bill_id, 'lab_assistant_id': lab_appointment_lab_assistant_id, 'cancelled': lab_appointment_cancelled, 'doctor_id': lab_appointment_doctor_id})
        refund_refund_id = argv['Op_Receptionist_cancelLabAppointment_run_8455']['newRefundId']
        refund_bill_id = state['TABLE_lab_appointment'].get({'lab_appointment_id': argv['Op_Receptionist_cancelLabAppointment_run_8455']['labAppointmentId']}, 'bill_id')
        refund_payment_type = StringVal('docApp')
        refund_reason = StringVal('no_reason')
        refund_amount = state['TABLE_bill'].get({'bill_id': state['TABLE_lab_appointment'].get({'lab_appointment_id': argv['Op_Receptionist_cancelLabAppointment_run_8455']['labAppointmentId']}, 'bill_id')}, 'total')
        refund_date = argv['Op_Receptionist_cancelLabAppointment_run_8455']['now']
        state['TABLE_refund'].add({'refund_id': refund_refund_id}, {'bill_id': refund_bill_id,'payment_type': refund_payment_type,'reason': refund_reason,'amount': refund_amount,'date': refund_date})
        return state

    def cond2(self, state, argv):
        labAppointmentId = argv['Op_Receptionist_cancelLabAppointment_run_8455']['labAppointmentId']
        lab_appointment_lab_appointment_id = argv['Op_Receptionist_cancelLabAppointment_run_8455']['lab_appointment_lab_appointment_id']
        lab_appointment_bill_id = argv['Op_Receptionist_cancelLabAppointment_run_8455']['lab_appointment_bill_id']
        newRefundId = argv['Op_Receptionist_cancelLabAppointment_run_8455']['newRefundId']
        bill_total = argv['Op_Receptionist_cancelLabAppointment_run_8455']['bill_total']
        now = argv['Op_Receptionist_cancelLabAppointment_run_8455']['now']
        bill_bill_id = argv['Op_Receptionist_cancelLabAppointment_run_8455']['bill_bill_id']
        return And((state['TABLE_lab_appointment'].notNil({'lab_appointment_id': argv['Op_Receptionist_cancelLabAppointment_run_8455']['labAppointmentId']}) == True),(state['TABLE_lab_appointment'].notNil({'lab_appointment_id': argv['Op_Receptionist_cancelLabAppointment_run_8455']['labAppointmentId']}) == True),(state['TABLE_bill'].notNil({'bill_id': state['TABLE_lab_appointment'].get({'lab_appointment_id': argv['Op_Receptionist_cancelLabAppointment_run_8455']['labAppointmentId']}, 'bill_id')}) == True),(state['TABLE_bill'].notNil({'bill_id': state['TABLE_lab_appointment'].get({'lab_appointment_id': argv['Op_Receptionist_cancelLabAppointment_run_8455']['labAppointmentId']}, 'bill_id')}) == True))

    def csop2(self, state, argv):
        return True

    def sop2(self, state, argv):
        labAppointmentId = argv['Op_Receptionist_cancelLabAppointment_run_8455']['labAppointmentId']
        lab_appointment_lab_appointment_id = argv['Op_Receptionist_cancelLabAppointment_run_8455']['lab_appointment_lab_appointment_id']
        lab_appointment_bill_id = argv['Op_Receptionist_cancelLabAppointment_run_8455']['lab_appointment_bill_id']
        newRefundId = argv['Op_Receptionist_cancelLabAppointment_run_8455']['newRefundId']
        bill_total = argv['Op_Receptionist_cancelLabAppointment_run_8455']['bill_total']
        now = argv['Op_Receptionist_cancelLabAppointment_run_8455']['now']
        bill_bill_id = argv['Op_Receptionist_cancelLabAppointment_run_8455']['bill_bill_id']
        lab_appointment_lab_appointment_id = state['TABLE_lab_appointment'].get({'lab_appointment_id': argv['Op_Receptionist_cancelLabAppointment_run_8455']['labAppointmentId']}, 'lab_appointment_id')
        lab_appointment_test_id = state['TABLE_lab_appointment'].get({'lab_appointment_id': argv['Op_Receptionist_cancelLabAppointment_run_8455']['labAppointmentId']}, 'test_id')
        lab_appointment_date = state['TABLE_lab_appointment'].get({'lab_appointment_id': argv['Op_Receptionist_cancelLabAppointment_run_8455']['labAppointmentId']}, 'date')
        lab_appointment_info = state['TABLE_lab_appointment'].get({'lab_appointment_id': argv['Op_Receptionist_cancelLabAppointment_run_8455']['labAppointmentId']}, 'info')
        lab_appointment_patient_id = state['TABLE_lab_appointment'].get({'lab_appointment_id': argv['Op_Receptionist_cancelLabAppointment_run_8455']['labAppointmentId']}, 'patient_id')
        lab_appointment_bill_id = state['TABLE_lab_appointment'].get({'lab_appointment_id': argv['Op_Receptionist_cancelLabAppointment_run_8455']['labAppointmentId']}, 'bill_id')
        lab_appointment_lab_assistant_id = state['TABLE_lab_appointment'].get({'lab_appointment_id': argv['Op_Receptionist_cancelLabAppointment_run_8455']['labAppointmentId']}, 'lab_assistant_id')
        lab_appointment_cancelled = state['TABLE_lab_appointment'].get({'lab_appointment_id': argv['Op_Receptionist_cancelLabAppointment_run_8455']['labAppointmentId']}, 'cancelled')
        lab_appointment_doctor_id = state['TABLE_lab_appointment'].get({'lab_appointment_id': argv['Op_Receptionist_cancelLabAppointment_run_8455']['labAppointmentId']}, 'doctor_id')
        lab_appointment_cancelled = True
        state['TABLE_lab_appointment'].update({'lab_appointment_id': argv['Op_Receptionist_cancelLabAppointment_run_8455']['labAppointmentId']}, {'lab_appointment_id': lab_appointment_lab_appointment_id, 'test_id': lab_appointment_test_id, 'date': lab_appointment_date, 'info': lab_appointment_info, 'patient_id': lab_appointment_patient_id, 'bill_id': lab_appointment_bill_id, 'lab_assistant_id': lab_appointment_lab_assistant_id, 'cancelled': lab_appointment_cancelled, 'doctor_id': lab_appointment_doctor_id})
        refund_refund_id = argv['Op_Receptionist_cancelLabAppointment_run_8455']['newRefundId']
        refund_bill_id = state['TABLE_lab_appointment'].get({'lab_appointment_id': argv['Op_Receptionist_cancelLabAppointment_run_8455']['labAppointmentId']}, 'bill_id')
        refund_payment_type = StringVal('docApp')
        refund_reason = StringVal('no_reason')
        refund_amount = state['TABLE_bill'].get({'bill_id': state['TABLE_lab_appointment'].get({'lab_appointment_id': argv['Op_Receptionist_cancelLabAppointment_run_8455']['labAppointmentId']}, 'bill_id')}, 'total')
        refund_date = argv['Op_Receptionist_cancelLabAppointment_run_8455']['now']
        state['TABLE_refund'].add({'refund_id': refund_refund_id}, {'bill_id': refund_bill_id,'payment_type': refund_payment_type,'reason': refund_reason,'amount': refund_amount,'date': refund_date})
        bill_bill_id = state['TABLE_bill'].get({'bill_id': state['TABLE_lab_appointment'].get({'lab_appointment_id': argv['Op_Receptionist_cancelLabAppointment_run_8455']['labAppointmentId']}, 'bill_id')}, 'bill_id')
        bill_bill_date = state['TABLE_bill'].get({'bill_id': state['TABLE_lab_appointment'].get({'lab_appointment_id': argv['Op_Receptionist_cancelLabAppointment_run_8455']['labAppointmentId']}, 'bill_id')}, 'bill_date')
        bill_doctor_fee = state['TABLE_bill'].get({'bill_id': state['TABLE_lab_appointment'].get({'lab_appointment_id': argv['Op_Receptionist_cancelLabAppointment_run_8455']['labAppointmentId']}, 'bill_id')}, 'doctor_fee')
        bill_hospital_fee = state['TABLE_bill'].get({'bill_id': state['TABLE_lab_appointment'].get({'lab_appointment_id': argv['Op_Receptionist_cancelLabAppointment_run_8455']['labAppointmentId']}, 'bill_id')}, 'hospital_fee')
        bill_pharmacy_fee = state['TABLE_bill'].get({'bill_id': state['TABLE_lab_appointment'].get({'lab_appointment_id': argv['Op_Receptionist_cancelLabAppointment_run_8455']['labAppointmentId']}, 'bill_id')}, 'pharmacy_fee')
        bill_laboratory_fee = state['TABLE_bill'].get({'bill_id': state['TABLE_lab_appointment'].get({'lab_appointment_id': argv['Op_Receptionist_cancelLabAppointment_run_8455']['labAppointmentId']}, 'bill_id')}, 'laboratory_fee')
        bill_appointment_fee = state['TABLE_bill'].get({'bill_id': state['TABLE_lab_appointment'].get({'lab_appointment_id': argv['Op_Receptionist_cancelLabAppointment_run_8455']['labAppointmentId']}, 'bill_id')}, 'appointment_fee')
        bill_vat = state['TABLE_bill'].get({'bill_id': state['TABLE_lab_appointment'].get({'lab_appointment_id': argv['Op_Receptionist_cancelLabAppointment_run_8455']['labAppointmentId']}, 'bill_id')}, 'vat')
        bill_discount = state['TABLE_bill'].get({'bill_id': state['TABLE_lab_appointment'].get({'lab_appointment_id': argv['Op_Receptionist_cancelLabAppointment_run_8455']['labAppointmentId']}, 'bill_id')}, 'discount')
        bill_total = state['TABLE_bill'].get({'bill_id': state['TABLE_lab_appointment'].get({'lab_appointment_id': argv['Op_Receptionist_cancelLabAppointment_run_8455']['labAppointmentId']}, 'bill_id')}, 'total')
        bill_payment_method = state['TABLE_bill'].get({'bill_id': state['TABLE_lab_appointment'].get({'lab_appointment_id': argv['Op_Receptionist_cancelLabAppointment_run_8455']['labAppointmentId']}, 'bill_id')}, 'payment_method')
        bill_consultant_id = state['TABLE_bill'].get({'bill_id': state['TABLE_lab_appointment'].get({'lab_appointment_id': argv['Op_Receptionist_cancelLabAppointment_run_8455']['labAppointmentId']}, 'bill_id')}, 'consultant_id')
        bill_patient_id = state['TABLE_bill'].get({'bill_id': state['TABLE_lab_appointment'].get({'lab_appointment_id': argv['Op_Receptionist_cancelLabAppointment_run_8455']['labAppointmentId']}, 'bill_id')}, 'patient_id')
        bill_refund = state['TABLE_bill'].get({'bill_id': state['TABLE_lab_appointment'].get({'lab_appointment_id': argv['Op_Receptionist_cancelLabAppointment_run_8455']['labAppointmentId']}, 'bill_id')}, 'refund')
        bill_refund = 1
        state['TABLE_bill'].update({'bill_id': state['TABLE_lab_appointment'].get({'lab_appointment_id': argv['Op_Receptionist_cancelLabAppointment_run_8455']['labAppointmentId']}, 'bill_id')}, {'bill_id': bill_bill_id, 'bill_date': bill_bill_date, 'doctor_fee': bill_doctor_fee, 'hospital_fee': bill_hospital_fee, 'pharmacy_fee': bill_pharmacy_fee, 'laboratory_fee': bill_laboratory_fee, 'appointment_fee': bill_appointment_fee, 'vat': bill_vat, 'discount': bill_discount, 'total': bill_total, 'payment_method': bill_payment_method, 'consultant_id': bill_consultant_id, 'patient_id': bill_patient_id, 'refund': bill_refund})
        return state


class Op_Pharmacist_addNewBrand_run_8456():
    def __init__(self):
        self.sops = [(self.cond0, self.csop0, self.sop0)]
        self.axiom = AxiomEmpty()

    def cond0(self, state, argv):
        newBrandId = argv['Op_Pharmacist_addNewBrand_run_8456']['newBrandId']
        brandName = argv['Op_Pharmacist_addNewBrand_run_8456']['brandName']
        genericName = argv['Op_Pharmacist_addNewBrand_run_8456']['genericName']
        drugType = argv['Op_Pharmacist_addNewBrand_run_8456']['drugType']
        drugUnit = argv['Op_Pharmacist_addNewBrand_run_8456']['drugUnit']
        unitPrice = argv['Op_Pharmacist_addNewBrand_run_8456']['unitPrice']
        return (state['TABLE_drug_brand_names'].notNil({'brand_id': argv['Op_Pharmacist_addNewBrand_run_8456']['newBrandId']}) == False)

    def csop0(self, state, argv):
        return True

    def sop0(self, state, argv):
        newBrandId = argv['Op_Pharmacist_addNewBrand_run_8456']['newBrandId']
        brandName = argv['Op_Pharmacist_addNewBrand_run_8456']['brandName']
        genericName = argv['Op_Pharmacist_addNewBrand_run_8456']['genericName']
        drugType = argv['Op_Pharmacist_addNewBrand_run_8456']['drugType']
        drugUnit = argv['Op_Pharmacist_addNewBrand_run_8456']['drugUnit']
        unitPrice = argv['Op_Pharmacist_addNewBrand_run_8456']['unitPrice']
        drug_brand_names_brand_id = argv['Op_Pharmacist_addNewBrand_run_8456']['newBrandId']
        drug_brand_names_brand_name = argv['Op_Pharmacist_addNewBrand_run_8456']['brandName']
        drug_brand_names_generic_name = argv['Op_Pharmacist_addNewBrand_run_8456']['genericName']
        drug_brand_names_drug_type = argv['Op_Pharmacist_addNewBrand_run_8456']['drugType']
        drug_brand_names_drug_unit = argv['Op_Pharmacist_addNewBrand_run_8456']['drugUnit']
        drug_brand_names_unit_price = argv['Op_Pharmacist_addNewBrand_run_8456']['unitPrice']
        state['TABLE_drug_brand_names'].add({'brand_id': drug_brand_names_brand_id}, {'brand_name': drug_brand_names_brand_name,'generic_name': drug_brand_names_generic_name,'drug_type': drug_brand_names_drug_type,'drug_unit': drug_brand_names_drug_unit,'unit_price': drug_brand_names_unit_price})
        return state


class Op_LabAssistant_SeriumCreatinePhosphokinase_run_8457():
    def __init__(self):
        self.sops = [(self.cond0, self.csop0, self.sop0)]
        self.axiom = AxiomEmpty()

    def cond0(self, state, argv):
        newTstId = argv['Op_LabAssistant_SeriumCreatinePhosphokinase_run_8457']['newTstId']
        appId = argv['Op_LabAssistant_SeriumCreatinePhosphokinase_run_8457']['appId']
        hiv12ELISA = argv['Op_LabAssistant_SeriumCreatinePhosphokinase_run_8457']['hiv12ELISA']
        now = argv['Op_LabAssistant_SeriumCreatinePhosphokinase_run_8457']['now']
        return (state['TABLE_SeriumCreatinePhosphokinase'].notNil({'tst_SCP_id': argv['Op_LabAssistant_SeriumCreatinePhosphokinase_run_8457']['newTstId']}) == False)

    def csop0(self, state, argv):
        return True

    def sop0(self, state, argv):
        newTstId = argv['Op_LabAssistant_SeriumCreatinePhosphokinase_run_8457']['newTstId']
        appId = argv['Op_LabAssistant_SeriumCreatinePhosphokinase_run_8457']['appId']
        hiv12ELISA = argv['Op_LabAssistant_SeriumCreatinePhosphokinase_run_8457']['hiv12ELISA']
        now = argv['Op_LabAssistant_SeriumCreatinePhosphokinase_run_8457']['now']
        SeriumCreatinePhosphokinase_tst_SCP_id = argv['Op_LabAssistant_SeriumCreatinePhosphokinase_run_8457']['newTstId']
        SeriumCreatinePhosphokinase_appointment_id = argv['Op_LabAssistant_SeriumCreatinePhosphokinase_run_8457']['appId']
        SeriumCreatinePhosphokinase_hiv12ELISA = argv['Op_LabAssistant_SeriumCreatinePhosphokinase_run_8457']['hiv12ELISA']
        SeriumCreatinePhosphokinase_date = argv['Op_LabAssistant_SeriumCreatinePhosphokinase_run_8457']['now']
        state['TABLE_SeriumCreatinePhosphokinase'].add({'tst_SCP_id': SeriumCreatinePhosphokinase_tst_SCP_id}, {'appointment_id': SeriumCreatinePhosphokinase_appointment_id,'hiv12ELISA': SeriumCreatinePhosphokinase_hiv12ELISA,'date': SeriumCreatinePhosphokinase_date})
        return state


class Op_Doctor_removeDoctorTime_run_8458():
    def __init__(self):
        self.sops = [(self.cond0, self.csop0, self.sop0)]
        self.axiom = AxiomEmpty()

    def cond0(self, state, argv):
        id = argv['Op_Doctor_removeDoctorTime_run_8458']['id']
        return True

    def csop0(self, state, argv):
        return True

    def sop0(self, state, argv):
        id = argv['Op_Doctor_removeDoctorTime_run_8458']['id']
        state['TABLE_doctor_availability'].delete({'time_slot_id': argv['Op_Doctor_removeDoctorTime_run_8458']['id']})
        return state


class Op_Admin_updateAccountInfo_run_8459():
    def __init__(self):
        self.sops = [(self.cond0, self.csop0, self.sop0)]
        self.axiom = AxiomEmpty()

    def cond0(self, state, argv):
        id = argv['Op_Admin_updateAccountInfo_run_8459']['id']
        sys_user_user_id = argv['Op_Admin_updateAccountInfo_run_8459']['sys_user_user_id']
        return (state['TABLE_sys_user'].notNil({'user_id': argv['Op_Admin_updateAccountInfo_run_8459']['id']}) == True)

    def csop0(self, state, argv):
        return True

    def sop0(self, state, argv):
        id = argv['Op_Admin_updateAccountInfo_run_8459']['id']
        sys_user_user_id = argv['Op_Admin_updateAccountInfo_run_8459']['sys_user_user_id']
        sys_user_person_id = state['TABLE_sys_user'].get({'user_id': argv['Op_Admin_updateAccountInfo_run_8459']['id']}, 'person_id')
        sys_user_user_id = state['TABLE_sys_user'].get({'user_id': argv['Op_Admin_updateAccountInfo_run_8459']['id']}, 'user_id')
        sys_user_user_name = state['TABLE_sys_user'].get({'user_id': argv['Op_Admin_updateAccountInfo_run_8459']['id']}, 'user_name')
        sys_user_user_type = state['TABLE_sys_user'].get({'user_id': argv['Op_Admin_updateAccountInfo_run_8459']['id']}, 'user_type')
        sys_user_other_info = state['TABLE_sys_user'].get({'user_id': argv['Op_Admin_updateAccountInfo_run_8459']['id']}, 'other_info')
        sys_user_password = state['TABLE_sys_user'].get({'user_id': argv['Op_Admin_updateAccountInfo_run_8459']['id']}, 'password')
        sys_user_online = state['TABLE_sys_user'].get({'user_id': argv['Op_Admin_updateAccountInfo_run_8459']['id']}, 'online')
        sys_user_login = state['TABLE_sys_user'].get({'user_id': argv['Op_Admin_updateAccountInfo_run_8459']['id']}, 'login')
        sys_user_logout = state['TABLE_sys_user'].get({'user_id': argv['Op_Admin_updateAccountInfo_run_8459']['id']}, 'logout')
        sys_user_profile_pic = state['TABLE_sys_user'].get({'user_id': argv['Op_Admin_updateAccountInfo_run_8459']['id']}, 'profile_pic')
        sys_user_suspend = state['TABLE_sys_user'].get({'user_id': argv['Op_Admin_updateAccountInfo_run_8459']['id']}, 'suspend')
        sys_user_other_info = argv['Op_Admin_updateAccountInfo_run_8459']['id']
        state['TABLE_sys_user'].update({'user_id': argv['Op_Admin_updateAccountInfo_run_8459']['id']}, {'person_id': sys_user_person_id, 'user_id': sys_user_user_id, 'user_name': sys_user_user_name, 'user_type': sys_user_user_type, 'other_info': sys_user_other_info, 'password': sys_user_password, 'online': sys_user_online, 'login': sys_user_login, 'logout': sys_user_logout, 'profile_pic': sys_user_profile_pic, 'suspend': sys_user_suspend})
        return state


class Op_LabAssistant_updateAccountInfo_run_8460():
    def __init__(self):
        self.sops = [(self.cond0, self.csop0, self.sop0)]
        self.axiom = AxiomEmpty()

    def cond0(self, state, argv):
        id = argv['Op_LabAssistant_updateAccountInfo_run_8460']['id']
        doctor_user_id = argv['Op_LabAssistant_updateAccountInfo_run_8460']['doctor_user_id']
        sys_user_user_id = argv['Op_LabAssistant_updateAccountInfo_run_8460']['sys_user_user_id']
        return And((state['TABLE_doctor'].notNil({'slmc_reg_no': argv['Op_LabAssistant_updateAccountInfo_run_8460']['id']}) == True),(state['TABLE_sys_user'].notNil({'user_id': state['TABLE_doctor'].get({'slmc_reg_no': argv['Op_LabAssistant_updateAccountInfo_run_8460']['id']}, 'user_id')}) == True))

    def csop0(self, state, argv):
        return True

    def sop0(self, state, argv):
        id = argv['Op_LabAssistant_updateAccountInfo_run_8460']['id']
        doctor_user_id = argv['Op_LabAssistant_updateAccountInfo_run_8460']['doctor_user_id']
        sys_user_user_id = argv['Op_LabAssistant_updateAccountInfo_run_8460']['sys_user_user_id']
        sys_user_person_id = state['TABLE_sys_user'].get({'user_id': state['TABLE_doctor'].get({'slmc_reg_no': argv['Op_LabAssistant_updateAccountInfo_run_8460']['id']}, 'user_id')}, 'person_id')
        sys_user_user_id = state['TABLE_sys_user'].get({'user_id': state['TABLE_doctor'].get({'slmc_reg_no': argv['Op_LabAssistant_updateAccountInfo_run_8460']['id']}, 'user_id')}, 'user_id')
        sys_user_user_name = state['TABLE_sys_user'].get({'user_id': state['TABLE_doctor'].get({'slmc_reg_no': argv['Op_LabAssistant_updateAccountInfo_run_8460']['id']}, 'user_id')}, 'user_name')
        sys_user_user_type = state['TABLE_sys_user'].get({'user_id': state['TABLE_doctor'].get({'slmc_reg_no': argv['Op_LabAssistant_updateAccountInfo_run_8460']['id']}, 'user_id')}, 'user_type')
        sys_user_other_info = state['TABLE_sys_user'].get({'user_id': state['TABLE_doctor'].get({'slmc_reg_no': argv['Op_LabAssistant_updateAccountInfo_run_8460']['id']}, 'user_id')}, 'other_info')
        sys_user_password = state['TABLE_sys_user'].get({'user_id': state['TABLE_doctor'].get({'slmc_reg_no': argv['Op_LabAssistant_updateAccountInfo_run_8460']['id']}, 'user_id')}, 'password')
        sys_user_online = state['TABLE_sys_user'].get({'user_id': state['TABLE_doctor'].get({'slmc_reg_no': argv['Op_LabAssistant_updateAccountInfo_run_8460']['id']}, 'user_id')}, 'online')
        sys_user_login = state['TABLE_sys_user'].get({'user_id': state['TABLE_doctor'].get({'slmc_reg_no': argv['Op_LabAssistant_updateAccountInfo_run_8460']['id']}, 'user_id')}, 'login')
        sys_user_logout = state['TABLE_sys_user'].get({'user_id': state['TABLE_doctor'].get({'slmc_reg_no': argv['Op_LabAssistant_updateAccountInfo_run_8460']['id']}, 'user_id')}, 'logout')
        sys_user_profile_pic = state['TABLE_sys_user'].get({'user_id': state['TABLE_doctor'].get({'slmc_reg_no': argv['Op_LabAssistant_updateAccountInfo_run_8460']['id']}, 'user_id')}, 'profile_pic')
        sys_user_suspend = state['TABLE_sys_user'].get({'user_id': state['TABLE_doctor'].get({'slmc_reg_no': argv['Op_LabAssistant_updateAccountInfo_run_8460']['id']}, 'user_id')}, 'suspend')
        sys_user_other_info = argv['Op_LabAssistant_updateAccountInfo_run_8460']['id']
        state['TABLE_sys_user'].update({'user_id': state['TABLE_doctor'].get({'slmc_reg_no': argv['Op_LabAssistant_updateAccountInfo_run_8460']['id']}, 'user_id')}, {'person_id': sys_user_person_id, 'user_id': sys_user_user_id, 'user_name': sys_user_user_name, 'user_type': sys_user_user_type, 'other_info': sys_user_other_info, 'password': sys_user_password, 'online': sys_user_online, 'login': sys_user_login, 'logout': sys_user_logout, 'profile_pic': sys_user_profile_pic, 'suspend': sys_user_suspend})
        return state


class Op_Cashier_updateProfileInfo_run_8461():
    def __init__(self):
        self.sops = [(self.cond0, self.csop0, self.sop0)]
        self.axiom = AxiomEmpty()

    def cond0(self, state, argv):
        id = argv['Op_Cashier_updateProfileInfo_run_8461']['id']
        sys_user_person_id = argv['Op_Cashier_updateProfileInfo_run_8461']['sys_user_person_id']
        return (state['TABLE_sys_user'].notNil({'user_id': argv['Op_Cashier_updateProfileInfo_run_8461']['id']}) == True)

    def csop0(self, state, argv):
        return True

    def sop0(self, state, argv):
        id = argv['Op_Cashier_updateProfileInfo_run_8461']['id']
        sys_user_person_id = argv['Op_Cashier_updateProfileInfo_run_8461']['sys_user_person_id']
        return state


class HealthPlus():
    def __init__(self):
        self.ops = [Op_Doctor_doctorTimeTableAddSlot_run_8412(),Op_Pharmacist_addNewDrug2_run_8413(),Op_Cashier_bill_run_8414(),Op_Pharmacist_updateStock_run_8415(),Op_Pharmacist_reduceStock_run_8416(),Op_LabAssistant_updateLabAssistantInfo_run_8417(),Op_Receptionist_updateAccountInfo_run_8418(),Op_Doctor_diagnose_run_8419(),Op_Pharmacist_updateAccountInfo_run_8420(),Op_LabAssistant_UrineFullReport_run_8421(),Op_Receptionist_cancelAppointment_run_8422(),Op_Cashier_makeRefund_run_8423(),Op_Cashier_refund_run_8424(),Op_Doctor_allergies_run_8425(),Op_Admin_createNewUser_run_8426(),Op_Pharmacist_bill_run_8427(),Op_Receptionist_updatePatientInfo_run_8428(),Op_Doctor_updateDoctorInfo_run_8429(),Op_Receptionist_updateProfileInfo_run_8430(),Op_LabAssistant_SeriumCreatinePhosphokinaseTotal_run_8431(),Op_Cashier_updateAccountInfo_run_8432(),Op_Admin_suspendUser_run_8433(),Op_Doctor_updateProfileInfo_run_8434(),Op_Pharmacist_updateProfileInfo_run_8435(),Op_Doctor_bill_run_8436(),Op_LabAssistant_BloodGroupingTest_run_8437(),Op_Doctor_prescribe_run_8438(),Op_Receptionist_setPatientInfo_run_8439(),Op_LabAssistant_RenalFunctionTest_run_8440(),Op_Admin_updateProfileInfo_run_8441(),Op_Admin_resetPassword_run_8442(),Op_Receptionist_refund_run_8443(),Op_Admin_unsuspendUser_run_8444(),Op_Receptionist_makeLabAppointment_run_8445(),Op_LabAssistant_LipidTest_run_8446(),Op_Doctor_updateAccountInfo_run_8447(),Op_LabAssistant_completeBloodCount_run_8448(),Op_Receptionist_makeAppointment_run_8449(),Op_Pharmacist_addNewSupplier_run_8450(),Op_Pharmacist_updatePharmacistInfo_run_8451(),Op_LabAssistant_updateProfileInfo_run_8452(),Op_Cashier_removeFromTempBill_run_8453(),Op_LabAssistant_liverFunctionTest_run_8454(),Op_Receptionist_cancelLabAppointment_run_8455(),Op_Pharmacist_addNewBrand_run_8456(),Op_LabAssistant_SeriumCreatinePhosphokinase_run_8457(),Op_Doctor_removeDoctorTime_run_8458(),Op_Admin_updateAccountInfo_run_8459(),Op_LabAssistant_updateAccountInfo_run_8460(),Op_Cashier_updateProfileInfo_run_8461()]
        self.tables = [BloodGroupingRh, LipidTest, LiverFunctionTest, RenalFunctionTest, SeriumCreatinePhosphokinase, SeriumCreatinePhosphokinaseTotal, UrineFullReport, appointment, bill, completeBloodCount, diagnose_history, doctor, doctor_availability, drug, drug_brand_names, lab_appointment, lab_appointment_timetable, lab_assistant, lab_test, medical_history, patient, patient_message_receive, patient_message_send, patient_useraccount, person, pharmacist, pharmacy_history, pharmacy_stock, prescription, refund, signup, suppliers, sys_user, tempappointment, tmp_bill, user_message, website_messages]
        self.state = GenState
        self.argv = GenArgv
        self.axiom = AxiomEmpty()

def factory():
    cls = globals()["HealthPlus"]
    return cls()

if __name__ == '__main__':
    check_parallel(factory, 8)

