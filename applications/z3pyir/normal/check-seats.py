import sys
sys.path.append("../../")

from z3 import *
from Rigi.axioms import *
from Rigi.checker import *
from Rigi.table import *
from Rigi.tableIns import *
from Rigi.argvbuilder import *

##############################################################################################

AIRLINE = Table('AIRLINE')
AIRLINE.addAttr('AL_ID', Table.Type.INT)
AIRLINE.addAttr('AL_IATA_CODE', Table.Type.STRING)
AIRLINE.addAttr('AL_ICAO_CODE', Table.Type.STRING)
AIRLINE.addAttr('AL_CALL_SIGN', Table.Type.STRING)
AIRLINE.addAttr('AL_NAME', Table.Type.STRING)
AIRLINE.addAttr('AL_CO_ID', Table.Type.INT)
AIRLINE.addAttr('AL_IATTR00', Table.Type.INT)
AIRLINE.addAttr('AL_IATTR01', Table.Type.INT)
AIRLINE.addAttr('AL_IATTR02', Table.Type.INT)
AIRLINE.addAttr('AL_IATTR03', Table.Type.INT)
AIRLINE.addAttr('AL_IATTR04', Table.Type.INT)
AIRLINE.addAttr('AL_IATTR05', Table.Type.INT)
AIRLINE.addAttr('AL_IATTR06', Table.Type.INT)
AIRLINE.addAttr('AL_IATTR07', Table.Type.INT)
AIRLINE.addAttr('AL_IATTR08', Table.Type.INT)
AIRLINE.addAttr('AL_IATTR09', Table.Type.INT)
AIRLINE.addAttr('AL_IATTR10', Table.Type.INT)
AIRLINE.addAttr('AL_IATTR11', Table.Type.INT)
AIRLINE.addAttr('AL_IATTR12', Table.Type.INT)
AIRLINE.addAttr('AL_IATTR13', Table.Type.INT)
AIRLINE.addAttr('AL_IATTR14', Table.Type.INT)
AIRLINE.addAttr('AL_IATTR15', Table.Type.INT)
AIRLINE.setPKey('AL_ID')
AIRLINE.build()


CONFIG_HISTOGRAMS = Table('CONFIG_HISTOGRAMS')
CONFIG_HISTOGRAMS.addAttr('CFH_NAME', Table.Type.STRING)
CONFIG_HISTOGRAMS.addAttr('CFH_DATA', Table.Type.STRING)
CONFIG_HISTOGRAMS.addAttr('CFH_IS_AIRPORT', Table.Type.INT)
CONFIG_HISTOGRAMS.setPKey('CFH_NAME')
CONFIG_HISTOGRAMS.build()


COUNTRY = Table('COUNTRY')
COUNTRY.addAttr('CO_ID', Table.Type.INT)
COUNTRY.addAttr('CO_NAME', Table.Type.STRING)
COUNTRY.addAttr('CO_CODE_2', Table.Type.STRING)
COUNTRY.addAttr('CO_CODE_3', Table.Type.STRING)
COUNTRY.setPKey('CO_ID')
COUNTRY.build()


AIRPORT = Table('AIRPORT')
AIRPORT.addAttr('AP_ID', Table.Type.INT)
AIRPORT.addAttr('AP_CODE', Table.Type.STRING)
AIRPORT.addAttr('AP_NAME', Table.Type.STRING)
AIRPORT.addAttr('AP_CITY', Table.Type.STRING)
AIRPORT.addAttr('AP_POSTAL_CODE', Table.Type.STRING)
AIRPORT.addAttr('AP_CO_ID', Table.Type.INT)
AIRPORT.addAttr('AP_INTEGERITUDE', Table.Type.REAL)
AIRPORT.addAttr('AP_LATITUDE', Table.Type.REAL)
AIRPORT.addAttr('AP_GMT_OFFSET', Table.Type.REAL)
AIRPORT.addAttr('AP_WAC', Table.Type.INT)
AIRPORT.addAttr('AP_IATTR00', Table.Type.INT)
AIRPORT.addAttr('AP_IATTR01', Table.Type.INT)
AIRPORT.addAttr('AP_IATTR02', Table.Type.INT)
AIRPORT.addAttr('AP_IATTR03', Table.Type.INT)
AIRPORT.addAttr('AP_IATTR04', Table.Type.INT)
AIRPORT.addAttr('AP_IATTR05', Table.Type.INT)
AIRPORT.addAttr('AP_IATTR06', Table.Type.INT)
AIRPORT.addAttr('AP_IATTR07', Table.Type.INT)
AIRPORT.addAttr('AP_IATTR08', Table.Type.INT)
AIRPORT.addAttr('AP_IATTR09', Table.Type.INT)
AIRPORT.addAttr('AP_IATTR10', Table.Type.INT)
AIRPORT.addAttr('AP_IATTR11', Table.Type.INT)
AIRPORT.addAttr('AP_IATTR12', Table.Type.INT)
AIRPORT.addAttr('AP_IATTR13', Table.Type.INT)
AIRPORT.addAttr('AP_IATTR14', Table.Type.INT)
AIRPORT.addAttr('AP_IATTR15', Table.Type.INT)
AIRPORT.setPKey('AP_ID')
AIRPORT.build()


FLIGHT = Table('FLIGHT')
FLIGHT.addAttr('F_ID', Table.Type.INT)
FLIGHT.addAttr('F_AL_ID', Table.Type.INT)
FLIGHT.addAttr('F_DEPART_AP_ID', Table.Type.INT)
FLIGHT.addAttr('F_DEPART_TIME', Table.Type.INT)
FLIGHT.addAttr('F_ARRIVE_AP_ID', Table.Type.INT)
FLIGHT.addAttr('F_ARRIVE_TIME', Table.Type.INT)
FLIGHT.addAttr('F_STATUS', Table.Type.INT)
FLIGHT.addAttr('F_BASE_PRICE', Table.Type.REAL)
FLIGHT.addAttr('F_SEATS_TOTAL', Table.Type.INT)
FLIGHT.addAttr('F_SEATS_LEFT', Table.Type.INT)
FLIGHT.addAttr('F_IATTR00', Table.Type.INT)
FLIGHT.addAttr('F_IATTR01', Table.Type.INT)
FLIGHT.addAttr('F_IATTR02', Table.Type.INT)
FLIGHT.addAttr('F_IATTR03', Table.Type.INT)
FLIGHT.addAttr('F_IATTR04', Table.Type.INT)
FLIGHT.addAttr('F_IATTR05', Table.Type.INT)
FLIGHT.addAttr('F_IATTR06', Table.Type.INT)
FLIGHT.addAttr('F_IATTR07', Table.Type.INT)
FLIGHT.addAttr('F_IATTR08', Table.Type.INT)
FLIGHT.addAttr('F_IATTR09', Table.Type.INT)
FLIGHT.addAttr('F_IATTR10', Table.Type.INT)
FLIGHT.addAttr('F_IATTR11', Table.Type.INT)
FLIGHT.addAttr('F_IATTR12', Table.Type.INT)
FLIGHT.addAttr('F_IATTR13', Table.Type.INT)
FLIGHT.addAttr('F_IATTR14', Table.Type.INT)
FLIGHT.addAttr('F_IATTR15', Table.Type.INT)
FLIGHT.addAttr('F_IATTR16', Table.Type.INT)
FLIGHT.addAttr('F_IATTR17', Table.Type.INT)
FLIGHT.addAttr('F_IATTR18', Table.Type.INT)
FLIGHT.addAttr('F_IATTR19', Table.Type.INT)
FLIGHT.addAttr('F_IATTR20', Table.Type.INT)
FLIGHT.addAttr('F_IATTR21', Table.Type.INT)
FLIGHT.addAttr('F_IATTR22', Table.Type.INT)
FLIGHT.addAttr('F_IATTR23', Table.Type.INT)
FLIGHT.addAttr('F_IATTR24', Table.Type.INT)
FLIGHT.addAttr('F_IATTR25', Table.Type.INT)
FLIGHT.addAttr('F_IATTR26', Table.Type.INT)
FLIGHT.addAttr('F_IATTR27', Table.Type.INT)
FLIGHT.addAttr('F_IATTR28', Table.Type.INT)
FLIGHT.addAttr('F_IATTR29', Table.Type.INT)
FLIGHT.setPKey('F_ID')
FLIGHT.build()


RESERVATION = Table('RESERVATION')
RESERVATION.addAttr('R_ID', Table.Type.INT)
RESERVATION.addAttr('R_C_ID', Table.Type.INT)
RESERVATION.addAttr('R_F_ID', Table.Type.INT)
RESERVATION.addAttr('R_SEAT', Table.Type.INT)
RESERVATION.addAttr('R_PRICE', Table.Type.REAL)
RESERVATION.addAttr('R_IATTR00', Table.Type.INT)
RESERVATION.addAttr('R_IATTR01', Table.Type.INT)
RESERVATION.addAttr('R_IATTR02', Table.Type.INT)
RESERVATION.addAttr('R_IATTR03', Table.Type.INT)
RESERVATION.addAttr('R_IATTR04', Table.Type.INT)
RESERVATION.addAttr('R_IATTR05', Table.Type.INT)
RESERVATION.addAttr('R_IATTR06', Table.Type.INT)
RESERVATION.addAttr('R_IATTR07', Table.Type.INT)
RESERVATION.addAttr('R_IATTR08', Table.Type.INT)
RESERVATION.setPKey('R_C_ID', 'R_F_ID')
RESERVATION.setPKey('R_F_ID', 'R_SEAT')
RESERVATION.setPKey('R_ID', 'R_C_ID', 'R_F_ID')
RESERVATION.setPKey('R_ID', 'R_C_ID', 'R_F_ID', 'R_SEAT')
RESERVATION.build()


CONFIG_PROFILE = Table('CONFIG_PROFILE')
CONFIG_PROFILE.addAttr('CFP_SCALE_FACTOR', Table.Type.REAL)
CONFIG_PROFILE.addAttr('CFP_AIPORT_MAX_CUSTOMER', Table.Type.STRING)
CONFIG_PROFILE.addAttr('CFP_FLIGHT_START', Table.Type.INT)
CONFIG_PROFILE.addAttr('CFP_FLIGHT_UPCOMING', Table.Type.INT)
CONFIG_PROFILE.addAttr('CFP_FLIGHT_PAST_DAYS', Table.Type.INT)
CONFIG_PROFILE.addAttr('CFP_FLIGHT_FUTURE_DAYS', Table.Type.INT)
CONFIG_PROFILE.addAttr('CFP_FLIGHT_OFFSET', Table.Type.INT)
CONFIG_PROFILE.addAttr('CFP_RESERVATION_OFFSET', Table.Type.INT)
CONFIG_PROFILE.addAttr('CFP_NUM_RESERVATIONS', Table.Type.INT)
CONFIG_PROFILE.addAttr('CFP_CODE_IDS_XREFS', Table.Type.STRING)
CONFIG_PROFILE.build()


AIRPORT_DISTANCE = Table('AIRPORT_DISTANCE')
AIRPORT_DISTANCE.addAttr('D_AP_ID0', Table.Type.INT)
AIRPORT_DISTANCE.addAttr('D_AP_ID1', Table.Type.INT)
AIRPORT_DISTANCE.addAttr('D_DISTANCE', Table.Type.REAL)
AIRPORT_DISTANCE.setPKey('D_AP_ID0')
AIRPORT_DISTANCE.setPKey('D_AP_ID1')
AIRPORT_DISTANCE.build()


CUSTOMER = Table('CUSTOMER')
CUSTOMER.addAttr('C_ID', Table.Type.INT)
CUSTOMER.addAttr('C_ID_STR', Table.Type.STRING)
CUSTOMER.addAttr('C_BASE_AP_ID', Table.Type.INT)
CUSTOMER.addAttr('C_BALANCE', Table.Type.REAL)
CUSTOMER.addAttr('C_SATTR00', Table.Type.STRING)
CUSTOMER.addAttr('C_SATTR01', Table.Type.STRING)
CUSTOMER.addAttr('C_SATTR02', Table.Type.STRING)
CUSTOMER.addAttr('C_SATTR03', Table.Type.STRING)
CUSTOMER.addAttr('C_SATTR04', Table.Type.STRING)
CUSTOMER.addAttr('C_SATTR05', Table.Type.STRING)
CUSTOMER.addAttr('C_SATTR06', Table.Type.STRING)
CUSTOMER.addAttr('C_SATTR07', Table.Type.STRING)
CUSTOMER.addAttr('C_SATTR08', Table.Type.STRING)
CUSTOMER.addAttr('C_SATTR09', Table.Type.STRING)
CUSTOMER.addAttr('C_SATTR10', Table.Type.STRING)
CUSTOMER.addAttr('C_SATTR11', Table.Type.STRING)
CUSTOMER.addAttr('C_SATTR12', Table.Type.STRING)
CUSTOMER.addAttr('C_SATTR13', Table.Type.STRING)
CUSTOMER.addAttr('C_SATTR14', Table.Type.STRING)
CUSTOMER.addAttr('C_SATTR15', Table.Type.STRING)
CUSTOMER.addAttr('C_SATTR16', Table.Type.STRING)
CUSTOMER.addAttr('C_SATTR17', Table.Type.STRING)
CUSTOMER.addAttr('C_SATTR18', Table.Type.STRING)
CUSTOMER.addAttr('C_SATTR19', Table.Type.STRING)
CUSTOMER.addAttr('C_IATTR00', Table.Type.INT)
CUSTOMER.addAttr('C_IATTR01', Table.Type.INT)
CUSTOMER.addAttr('C_IATTR02', Table.Type.INT)
CUSTOMER.addAttr('C_IATTR03', Table.Type.INT)
CUSTOMER.addAttr('C_IATTR04', Table.Type.INT)
CUSTOMER.addAttr('C_IATTR05', Table.Type.INT)
CUSTOMER.addAttr('C_IATTR06', Table.Type.INT)
CUSTOMER.addAttr('C_IATTR07', Table.Type.INT)
CUSTOMER.addAttr('C_IATTR08', Table.Type.INT)
CUSTOMER.addAttr('C_IATTR09', Table.Type.INT)
CUSTOMER.addAttr('C_IATTR10', Table.Type.INT)
CUSTOMER.addAttr('C_IATTR11', Table.Type.INT)
CUSTOMER.addAttr('C_IATTR12', Table.Type.INT)
CUSTOMER.addAttr('C_IATTR13', Table.Type.INT)
CUSTOMER.addAttr('C_IATTR14', Table.Type.INT)
CUSTOMER.addAttr('C_IATTR15', Table.Type.INT)
CUSTOMER.addAttr('C_IATTR16', Table.Type.INT)
CUSTOMER.addAttr('C_IATTR17', Table.Type.INT)
CUSTOMER.addAttr('C_IATTR18', Table.Type.INT)
CUSTOMER.addAttr('C_IATTR19', Table.Type.INT)
CUSTOMER.setPKey('C_ID')
CUSTOMER.setPKey('C_ID_STR')
CUSTOMER.build()


FREQUENT_FLYER = Table('FREQUENT_FLYER')
FREQUENT_FLYER.addAttr('FF_C_ID', Table.Type.INT)
FREQUENT_FLYER.addAttr('FF_AL_ID', Table.Type.INT)
FREQUENT_FLYER.addAttr('FF_C_ID_STR', Table.Type.STRING)
FREQUENT_FLYER.addAttr('FF_SATTR00', Table.Type.STRING)
FREQUENT_FLYER.addAttr('FF_SATTR01', Table.Type.STRING)
FREQUENT_FLYER.addAttr('FF_SATTR02', Table.Type.STRING)
FREQUENT_FLYER.addAttr('FF_SATTR03', Table.Type.STRING)
FREQUENT_FLYER.addAttr('FF_IATTR00', Table.Type.INT)
FREQUENT_FLYER.addAttr('FF_IATTR01', Table.Type.INT)
FREQUENT_FLYER.addAttr('FF_IATTR02', Table.Type.INT)
FREQUENT_FLYER.addAttr('FF_IATTR03', Table.Type.INT)
FREQUENT_FLYER.addAttr('FF_IATTR04', Table.Type.INT)
FREQUENT_FLYER.addAttr('FF_IATTR05', Table.Type.INT)
FREQUENT_FLYER.addAttr('FF_IATTR06', Table.Type.INT)
FREQUENT_FLYER.addAttr('FF_IATTR07', Table.Type.INT)
FREQUENT_FLYER.addAttr('FF_IATTR08', Table.Type.INT)
FREQUENT_FLYER.addAttr('FF_IATTR09', Table.Type.INT)
FREQUENT_FLYER.addAttr('FF_IATTR10', Table.Type.INT)
FREQUENT_FLYER.addAttr('FF_IATTR11', Table.Type.INT)
FREQUENT_FLYER.addAttr('FF_IATTR12', Table.Type.INT)
FREQUENT_FLYER.addAttr('FF_IATTR13', Table.Type.INT)
FREQUENT_FLYER.addAttr('FF_IATTR14', Table.Type.INT)
FREQUENT_FLYER.addAttr('FF_IATTR15', Table.Type.INT)
FREQUENT_FLYER.setPKey('FF_C_ID','FF_AL_ID')
FREQUENT_FLYER.build()


def GenState():
    TABLE_AIRLINE = TableInstance(AIRLINE)
    TABLE_CONFIG_HISTOGRAMS = TableInstance(CONFIG_HISTOGRAMS)
    TABLE_COUNTRY = TableInstance(COUNTRY)
    TABLE_AIRPORT = TableInstance(AIRPORT)
    TABLE_FLIGHT = TableInstance(FLIGHT)
    TABLE_RESERVATION = TableInstance(RESERVATION)
    TABLE_CONFIG_PROFILE = TableInstance(CONFIG_PROFILE)
    TABLE_AIRPORT_DISTANCE = TableInstance(AIRPORT_DISTANCE)
    TABLE_CUSTOMER = TableInstance(CUSTOMER)
    TABLE_FREQUENT_FLYER = TableInstance(FREQUENT_FLYER)
    return {'TABLE_AIRLINE':TABLE_AIRLINE,'TABLE_CONFIG_HISTOGRAMS':TABLE_CONFIG_HISTOGRAMS,'TABLE_COUNTRY':TABLE_COUNTRY,'TABLE_AIRPORT':TABLE_AIRPORT,'TABLE_FLIGHT':TABLE_FLIGHT,'TABLE_RESERVATION':TABLE_RESERVATION,'TABLE_CONFIG_PROFILE':TABLE_CONFIG_PROFILE,'TABLE_AIRPORT_DISTANCE':TABLE_AIRPORT_DISTANCE,'TABLE_CUSTOMER':TABLE_CUSTOMER,'TABLE_FREQUENT_FLYER':TABLE_FREQUENT_FLYER}

def GenArgv():
    builder = ArgvBuilder()
    builder.NewOp('UpdateReservation_run_84')
    builder.AddArgv('seatnum',ArgvBuilder.Type.INT)
    builder.AddArgv('attr_idx',ArgvBuilder.Type.INT)
    builder.AddArgv('c_id',ArgvBuilder.Type.INT)
    builder.AddArgv('attr_val',ArgvBuilder.Type.INT)
    builder.AddArgv('f_id',ArgvBuilder.Type.INT)
    builder.AddArgv('r_id',ArgvBuilder.Type.INT)
    
    builder.NewOp('UpdateCustomer_run_53')
    builder.AddArgv('attr0',ArgvBuilder.Type.INT)
    builder.AddArgv('c_id_str',ArgvBuilder.Type.STRING)
    builder.AddArgv('update_ff',ArgvBuilder.Type.INT)
    builder.AddArgv('c_id',ArgvBuilder.Type.INT)
    builder.AddArgv('attr1',ArgvBuilder.Type.INT)
    builder.AddArgv('ff_al_id',ArgvBuilder.Type.INT)

    builder.NewOp('NewReservation_run_116')
    builder.AddArgv('attrs8',ArgvBuilder.Type.INT)
    builder.AddArgv('attrs7',ArgvBuilder.Type.INT)
    builder.AddArgv('attrs6',ArgvBuilder.Type.INT)
    builder.AddArgv('attrs5',ArgvBuilder.Type.INT)
    builder.AddArgv('attrs4',ArgvBuilder.Type.INT)
    builder.AddArgv('attrs3',ArgvBuilder.Type.INT)
    builder.AddArgv('attrs2',ArgvBuilder.Type.INT)
    builder.AddArgv('attrs1',ArgvBuilder.Type.INT)
    builder.AddArgv('attrs0',ArgvBuilder.Type.INT)
    builder.AddArgv('seatnum',ArgvBuilder.Type.INT)
    builder.AddArgv('price',ArgvBuilder.Type.REAL)
    builder.AddArgv('c_id',ArgvBuilder.Type.INT)
    builder.AddArgv('f_id',ArgvBuilder.Type.INT)
    builder.AddArgv('r_id',ArgvBuilder.Type.INT)
    builder.AddArgv('airline_id',ArgvBuilder.Type.INT)

    builder.NewOp('DeleteReservation_run_59')
    builder.AddArgv('c_id_str',ArgvBuilder.Type.STRING)
    builder.AddArgv('c_id',ArgvBuilder.Type.INT)
    builder.AddArgv('ff_al_id',ArgvBuilder.Type.INT)
    builder.AddArgv('f_id',ArgvBuilder.Type.INT)
    builder.AddArgv('ff_c_id_str',ArgvBuilder.Type.STRING)
    builder.AddArgv('c_iattr10',ArgvBuilder.Type.INT)
    builder.AddArgv('c_iattr00',ArgvBuilder.Type.INT)
    builder.AddArgv('c_iattr11',ArgvBuilder.Type.INT)
    builder.AddArgv('r_id',ArgvBuilder.Type.INT)
    builder.AddArgv('r_price',ArgvBuilder.Type.REAL)
    builder.AddArgv('ff_itattr10',ArgvBuilder.Type.INT)

    return builder.Build()

class Op_UpdateReservation_run_84():
    def __init__(self):
        self.sops = [(self.cond0, self.csop0, self.sop0),(self.cond1, self.csop1, self.sop1),(self.cond2, self.csop2, self.sop2),(self.cond3, self.csop3, self.sop3)]
        self.axiom = AxiomEmpty()

    def cond0(self, state, argv):
        f_id = argv['UpdateReservation_run_84']['f_id']
        seatnum = argv['UpdateReservation_run_84']['seatnum']
        c_id = argv['UpdateReservation_run_84']['c_id']
        attr_idx = argv['UpdateReservation_run_84']['attr_idx']
        return And((Not(state['TABLE_RESERVATION'].notNil({'R_F_ID' : f_id,'R_SEAT' : seatnum}) == True)),(Not(state['TABLE_RESERVATION'].notNil({'R_F_ID' : f_id,'R_C_ID' : c_id}) == False)),((attr_idx == 0)))
    

    def csop0(self, state, argv):
        return True
    

    def sop0(self, state, argv):
        seatnum = argv['UpdateReservation_run_84']['seatnum']
        attr_val = argv['UpdateReservation_run_84']['attr_val']
        r_id = argv['UpdateReservation_run_84']['r_id']
        c_id = argv['UpdateReservation_run_84']['c_id']
        f_id = argv['UpdateReservation_run_84']['f_id']
        R_SEAT = state['TABLE_RESERVATION'].get({'R_ID' : r_id,'R_C_ID' : c_id,'R_F_ID' : f_id}, 'R_SEAT')
        R_IATTR00 = state['TABLE_RESERVATION'].get({'R_ID' : r_id,'R_C_ID' : c_id,'R_F_ID' : f_id}, 'R_IATTR00')
        R_SEAT = seatnum
        R_IATTR00 = attr_val
        state['TABLE_RESERVATION'].update({'R_ID' : r_id,'R_C_ID' : c_id,'R_F_ID' : f_id}, {'R_SEAT' : R_SEAT,'R_IATTR00' : R_IATTR00})
        return state


    def cond1(self, state, argv):
        f_id = argv['UpdateReservation_run_84']['f_id']
        seatnum = argv['UpdateReservation_run_84']['seatnum']
        c_id = argv['UpdateReservation_run_84']['c_id']
        attr_idx = argv['UpdateReservation_run_84']['attr_idx']
        return And((Not(state['TABLE_RESERVATION'].notNil({'R_F_ID' : f_id,'R_SEAT' : seatnum}) == True)),(Not(state['TABLE_RESERVATION'].notNil({'R_F_ID' : f_id,'R_C_ID' : c_id}) == False)),(Not(attr_idx == 0)),((attr_idx == 1)))
    

    def csop1(self, state, argv):
        return True
    

    def sop1(self, state, argv):
        seatnum = argv['UpdateReservation_run_84']['seatnum']
        attr_val = argv['UpdateReservation_run_84']['attr_val']
        r_id = argv['UpdateReservation_run_84']['r_id']
        c_id = argv['UpdateReservation_run_84']['c_id']
        f_id = argv['UpdateReservation_run_84']['f_id']
        R_SEAT = state['TABLE_RESERVATION'].get({'R_ID' : r_id,'R_C_ID' : c_id,'R_F_ID' : f_id}, 'R_SEAT')
        R_IATTR01 = state['TABLE_RESERVATION'].get({'R_ID' : r_id,'R_C_ID' : c_id,'R_F_ID' : f_id}, 'R_IATTR01')
        R_SEAT = seatnum
        R_IATTR01 = attr_val
        state['TABLE_RESERVATION'].update({'R_ID' : r_id,'R_C_ID' : c_id,'R_F_ID' : f_id}, {'R_SEAT' : R_SEAT,'R_IATTR01' : R_IATTR01})
        return state


    def cond2(self, state, argv):
        f_id = argv['UpdateReservation_run_84']['f_id']
        seatnum = argv['UpdateReservation_run_84']['seatnum']
        c_id = argv['UpdateReservation_run_84']['c_id']
        attr_idx = argv['UpdateReservation_run_84']['attr_idx']
        return And((Not(state['TABLE_RESERVATION'].notNil({'R_F_ID' : f_id,'R_SEAT' : seatnum}) == True)),(Not(state['TABLE_RESERVATION'].notNil({'R_F_ID' : f_id,'R_C_ID' : c_id}) == False)),(Not(attr_idx == 0)),(Not(attr_idx == 1)),((attr_idx == 2)))
    

    def csop2(self, state, argv):
        return True
    

    def sop2(self, state, argv):
        seatnum = argv['UpdateReservation_run_84']['seatnum']
        attr_val = argv['UpdateReservation_run_84']['attr_val']
        r_id = argv['UpdateReservation_run_84']['r_id']
        c_id = argv['UpdateReservation_run_84']['c_id']
        f_id = argv['UpdateReservation_run_84']['f_id']
        R_SEAT = state['TABLE_RESERVATION'].get({'R_ID' : r_id,'R_C_ID' : c_id,'R_F_ID' : f_id}, 'R_SEAT')
        R_IATTR02 = state['TABLE_RESERVATION'].get({'R_ID' : r_id,'R_C_ID' : c_id,'R_F_ID' : f_id}, 'R_IATTR02')
        R_SEAT = seatnum
        R_IATTR02 = attr_val
        state['TABLE_RESERVATION'].update({'R_ID' : r_id,'R_C_ID' : c_id,'R_F_ID' : f_id}, {'R_SEAT' : R_SEAT,'R_IATTR02' : R_IATTR02})
        return state


    def cond3(self, state, argv):
        f_id = argv['UpdateReservation_run_84']['f_id']
        seatnum = argv['UpdateReservation_run_84']['seatnum']
        c_id = argv['UpdateReservation_run_84']['c_id']
        attr_idx = argv['UpdateReservation_run_84']['attr_idx']
        return And((Not(state['TABLE_RESERVATION'].notNil({'R_F_ID' : f_id,'R_SEAT' : seatnum}) == True)),(Not(state['TABLE_RESERVATION'].notNil({'R_F_ID' : f_id,'R_C_ID' : c_id}) == False)),(Not(attr_idx == 0)),(Not(attr_idx == 1)),(Not(attr_idx == 2)),((attr_idx == 3)))
    

    def csop3(self, state, argv):
        return True
    

    def sop3(self, state, argv):
        seatnum = argv['UpdateReservation_run_84']['seatnum']
        attr_val = argv['UpdateReservation_run_84']['attr_val']
        r_id = argv['UpdateReservation_run_84']['r_id']
        c_id = argv['UpdateReservation_run_84']['c_id']
        f_id = argv['UpdateReservation_run_84']['f_id']
        R_SEAT = state['TABLE_RESERVATION'].get({'R_ID' : r_id,'R_C_ID' : c_id,'R_F_ID' : f_id}, 'R_SEAT')
        R_IATTR03 = state['TABLE_RESERVATION'].get({'R_ID' : r_id,'R_C_ID' : c_id,'R_F_ID' : f_id}, 'R_IATTR03')
        R_SEAT = seatnum
        R_IATTR03 = attr_val
        state['TABLE_RESERVATION'].update({'R_ID' : r_id,'R_C_ID' : c_id,'R_F_ID' : f_id}, {'R_SEAT' : R_SEAT,'R_IATTR03' : R_IATTR03})
        return state

class Op_UpdateCustomer_run_53():
    def __init__(self):
        self.sops = [(self.cond0, self.csop0, self.sop0),(self.cond1, self.csop1, self.sop1)]
        self.axiom = AxiomEmpty()


    def cond0(self, state, argv):
        c_id = argv['UpdateCustomer_run_53']['c_id']
        update_ff = argv['UpdateCustomer_run_53']['update_ff']
        return And((Not(And (state['TABLE_CUSTOMER'].notNil({'C_ID' : c_id}),state['TABLE_CUSTOMER'].get({'C_ID' : c_id}, 'C_ID')== c_id) == False)))
    

    def csop0(self, state, argv):
        return True
    

    def sop0(self, state, argv):
        attr0 = argv['UpdateCustomer_run_53']['attr0']
        attr1 = argv['UpdateCustomer_run_53']['attr1']
        c_id = argv['UpdateCustomer_run_53']['c_id']
        C_IATTR00 = state['TABLE_CUSTOMER'].get({'C_ID' : c_id}, 'C_IATTR00')
        C_IATTR01 = state['TABLE_CUSTOMER'].get({'C_ID' : c_id}, 'C_IATTR01')
        C_IATTR00 = attr0
        C_IATTR01 = attr1
        state['TABLE_CUSTOMER'].update({'C_ID' : c_id}, {'C_IATTR00' : C_IATTR00,'C_IATTR01' : C_IATTR01})
        return state


    def cond1(self, state, argv):
        c_id = argv['UpdateCustomer_run_53']['c_id']
        update_ff = argv['UpdateCustomer_run_53']['update_ff']
        return And((Not(And (state['TABLE_CUSTOMER'].notNil({'C_ID' : c_id}),state['TABLE_CUSTOMER'].get({'C_ID' : c_id}, 'C_ID')== c_id) == False)))
    

    def csop1(self, state, argv):
        return True
    

    def sop1(self, state, argv):
        attr0 = argv['UpdateCustomer_run_53']['attr0']
        attr1 = argv['UpdateCustomer_run_53']['attr1']
        c_id = argv['UpdateCustomer_run_53']['c_id']
        ff_al_id = argv['UpdateCustomer_run_53']['ff_al_id']
        FF_IATTR00 = state['TABLE_FREQUENT_FLYER'].get({'FF_C_ID' : c_id,'FF_AL_ID' : ff_al_id}, 'FF_IATTR00')
        FF_IATTR01 = state['TABLE_FREQUENT_FLYER'].get({'FF_C_ID' : c_id,'FF_AL_ID' : ff_al_id}, 'FF_IATTR01')
        FF_IATTR00 = attr0
        FF_IATTR01 = attr1
        state['TABLE_FREQUENT_FLYER'].update({'FF_C_ID' : c_id,'FF_AL_ID' : ff_al_id}, {'FF_IATTR00' : FF_IATTR00,'FF_IATTR01' : FF_IATTR01})
        attr0 = argv['UpdateCustomer_run_53']['attr0']
        attr1 = argv['UpdateCustomer_run_53']['attr1']
        c_id = argv['UpdateCustomer_run_53']['c_id']
        C_IATTR00 = state['TABLE_CUSTOMER'].get({'C_ID' : c_id}, 'C_IATTR00')
        C_IATTR01 = state['TABLE_CUSTOMER'].get({'C_ID' : c_id}, 'C_IATTR01')
        C_IATTR00 = attr0
        C_IATTR01 = attr1
        state['TABLE_CUSTOMER'].update({'C_ID' : c_id}, {'C_IATTR00' : C_IATTR00,'C_IATTR01' : C_IATTR01})
        return state

class Op_NewReservation_run_116():
    def __init__(self):
        self.sops = [(self.cond0, self.csop0, self.sop0)]
        self.axiom = AxiomEmpty()

    def cond0(self, state, argv):
        seatnum = argv['NewReservation_run_116']['seatnum']
        f_id = argv['NewReservation_run_116']['f_id']
        c_id = argv['NewReservation_run_116']['c_id']
        return And((Not(And (state['TABLE_FLIGHT'].notNil({'F_ID' : f_id}),state['TABLE_FLIGHT'].get({'F_ID' : f_id}, 'F_ID')== f_id) == False)),state['TABLE_RESERVATION'].notNil({'R_C_ID' : c_id,'R_F_ID' : f_id}) == False,(Not(state['TABLE_FLIGHT'].get({'F_ID' : f_id}, 'F_SEATS_LEFT') <= 0)),(Not(And (state['TABLE_RESERVATION'].notNil({'R_F_ID' : f_id,'R_SEAT' : seatnum}),state['TABLE_RESERVATION'].get({'R_F_ID' : f_id,'R_SEAT' : seatnum}, 'R_F_ID')== f_id,state['TABLE_RESERVATION'].get({'R_F_ID' : f_id,'R_SEAT' : seatnum}, 'R_SEAT')== seatnum) == True)),(Not(And (state['TABLE_RESERVATION'].notNil({'R_F_ID' : f_id,'R_C_ID' : c_id}),state['TABLE_RESERVATION'].get({'R_F_ID' : f_id,'R_C_ID' : c_id}, 'R_F_ID')== f_id,state['TABLE_RESERVATION'].get({'R_F_ID' : f_id,'R_C_ID' : c_id}, 'R_C_ID')== c_id) == True)),(Not(And (state['TABLE_CUSTOMER'].notNil({'C_ID' : c_id}),state['TABLE_CUSTOMER'].get({'C_ID' : c_id}, 'C_ID')== c_id) == False)))


    def csop0(self, state, argv):
        return True
    

    def sop0(self, state, argv):
        price = argv['NewReservation_run_116']['price']
        attrs0 = argv['NewReservation_run_116']['attrs0']
        attrs1 = argv['NewReservation_run_116']['attrs1']
        attrs2 = argv['NewReservation_run_116']['attrs2']
        attrs3 = argv['NewReservation_run_116']['attrs3']
        attrs4 = argv['NewReservation_run_116']['attrs4']
        attrs5 = argv['NewReservation_run_116']['attrs5']
        attrs6 = argv['NewReservation_run_116']['attrs6']
        attrs7 = argv['NewReservation_run_116']['attrs7']
        attrs8 = argv['NewReservation_run_116']['attrs8']
        r_id = argv['NewReservation_run_116']['r_id']
        c_id = argv['NewReservation_run_116']['c_id']
        f_id = argv['NewReservation_run_116']['f_id']
        seatnum = argv['NewReservation_run_116']['seatnum']
        R_ID = r_id
        R_C_ID = c_id
        R_F_ID = f_id
        R_SEAT = seatnum
        R_PRICE = price
        R_IATTR00 = attrs0
        R_IATTR01 = attrs1
        R_IATTR02 = attrs2
        R_IATTR03 = attrs3
        R_IATTR04 = attrs4
        R_IATTR05 = attrs5
        R_IATTR06 = attrs6
        R_IATTR07 = attrs7
        R_IATTR08 = attrs8
        state['TABLE_RESERVATION'].add({'R_C_ID' : c_id,'R_F_ID' : f_id}, {'R_ID' : r_id,'R_SEAT' : seatnum,'R_PRICE' : R_PRICE,'R_IATTR00' : R_IATTR00,'R_IATTR01' : R_IATTR01,'R_IATTR02' : R_IATTR02,'R_IATTR03' : R_IATTR03,'R_IATTR04' : R_IATTR04,'R_IATTR05' : R_IATTR05,'R_IATTR06' : R_IATTR06,'R_IATTR07' : R_IATTR07,'R_IATTR08' : R_IATTR08})
        f_id = argv['NewReservation_run_116']['f_id']
        c_id = argv['NewReservation_run_116']['c_id']
        F_SEATS_LEFT = state['TABLE_FLIGHT'].get({'F_ID' : c_id}, 'F_SEATS_LEFT')
        F_SEATS_LEFT = F_SEATS_LEFT - f_id
        state['TABLE_FLIGHT'].update({'F_ID' : c_id}, {'F_SEATS_LEFT' : F_SEATS_LEFT})
        attrs0 = argv['NewReservation_run_116']['attrs0']
        attrs1 = argv['NewReservation_run_116']['attrs1']
        attrs2 = argv['NewReservation_run_116']['attrs2']
        attrs3 = argv['NewReservation_run_116']['attrs3']
        c_id = argv['NewReservation_run_116']['c_id']
        attrs0 = argv['NewReservation_run_116']['attrs0']
        attrs1 = argv['NewReservation_run_116']['attrs1']
        C_IATTR10 = state['TABLE_CUSTOMER'].get({'C_ID' : attrs1}, 'C_IATTR10')
        C_IATTR11 = state['TABLE_CUSTOMER'].get({'C_ID' : attrs1}, 'C_IATTR11')
        C_IATTR12 = state['TABLE_CUSTOMER'].get({'C_ID' : attrs1}, 'C_IATTR12')
        C_IATTR13 = state['TABLE_CUSTOMER'].get({'C_ID' : attrs1}, 'C_IATTR13')
        C_IATTR14 = state['TABLE_CUSTOMER'].get({'C_ID' : attrs1}, 'C_IATTR14')
        C_IATTR15 = state['TABLE_CUSTOMER'].get({'C_ID' : attrs1}, 'C_IATTR15')
        C_IATTR10 = C_IATTR10 + attrs0
        C_IATTR11 = C_IATTR11 + attrs1
        C_IATTR12 = attrs2
        C_IATTR13 = attrs3
        C_IATTR14 = c_id
        C_IATTR15 = attrs0
        state['TABLE_CUSTOMER'].update({'C_ID' : attrs1}, {'C_IATTR10' : C_IATTR10,'C_IATTR11' : C_IATTR11,'C_IATTR12' : C_IATTR12,'C_IATTR13' : C_IATTR13,'C_IATTR14' : C_IATTR14,'C_IATTR15' : C_IATTR15})
        attrs4 = argv['NewReservation_run_116']['attrs4']
        attrs5 = argv['NewReservation_run_116']['attrs5']
        attrs6 = argv['NewReservation_run_116']['attrs6']
        attrs7 = argv['NewReservation_run_116']['attrs7']
        c_id = argv['NewReservation_run_116']['c_id']
        airline_id = argv['NewReservation_run_116']['airline_id']
        attrs1 = argv['NewReservation_run_116']['attrs1']
        FF_IATTR10 = state['TABLE_FREQUENT_FLYER'].get({'FF_C_ID' : airline_id,'FF_AL_ID' : attrs1}, 'FF_IATTR10')
        FF_IATTR11 = state['TABLE_FREQUENT_FLYER'].get({'FF_C_ID' : airline_id,'FF_AL_ID' : attrs1}, 'FF_IATTR11')
        FF_IATTR12 = state['TABLE_FREQUENT_FLYER'].get({'FF_C_ID' : airline_id,'FF_AL_ID' : attrs1}, 'FF_IATTR12')
        FF_IATTR13 = state['TABLE_FREQUENT_FLYER'].get({'FF_C_ID' : airline_id,'FF_AL_ID' : attrs1}, 'FF_IATTR13')
        FF_IATTR14 = state['TABLE_FREQUENT_FLYER'].get({'FF_C_ID' : airline_id,'FF_AL_ID' : attrs1}, 'FF_IATTR14')
        FF_IATTR10 = FF_IATTR10 + attrs4
        FF_IATTR11 = attrs5
        FF_IATTR12 = attrs6
        FF_IATTR13 = attrs7
        FF_IATTR14 = c_id
        state['TABLE_FREQUENT_FLYER'].update({'FF_C_ID' : airline_id,'FF_AL_ID' : attrs1}, {'FF_IATTR10' : FF_IATTR10,'FF_IATTR11' : FF_IATTR11,'FF_IATTR12' : FF_IATTR12,'FF_IATTR13' : FF_IATTR13,'FF_IATTR14' : FF_IATTR14})
        return state

class Op_DeleteReservation_run_59():
    def __init__(self):
        self.sops = [(self.cond0, self.csop0, self.sop0),(self.cond1, self.csop1, self.sop1)]
        self.axiom = AxiomEmpty()


    def cond0(self, state, argv):
        c_id = argv['DeleteReservation_run_59']['c_id']
        f_id = argv['DeleteReservation_run_59']['f_id']
        ff_al_id = argv['DeleteReservation_run_59']['ff_al_id']
        return And((Not(And (state['TABLE_CUSTOMER'].notNil({'C_ID' : c_id}),state['TABLE_CUSTOMER'].get({'C_ID' : c_id}, 'C_ID')== c_id) == False)),(Not(And (state['TABLE_FLIGHT'].notNil({'F_ID' : f_id}),state['TABLE_FLIGHT'].get({'F_ID' : f_id}, 'F_ID')== f_id) == False)),(Not(And (state['TABLE_RESERVATION'].notNil({'R_C_ID' : c_id,'R_F_ID' : f_id}),state['TABLE_RESERVATION'].get({'R_C_ID' : c_id,'R_F_ID' : f_id}, 'R_C_ID')== c_id,state['TABLE_RESERVATION'].get({'R_C_ID' : c_id,'R_F_ID' : f_id}, 'R_F_ID')== f_id) == False)))
    

    def csop0(self, state, argv):
        return True
    

    def sop0(self, state, argv):
        r_id = argv['DeleteReservation_run_59']['r_id']
        c_id = argv['DeleteReservation_run_59']['c_id']
        f_id = argv['DeleteReservation_run_59']['f_id']
        state['TABLE_RESERVATION'].delete({'R_ID' : r_id,'R_C_ID' : c_id,'R_F_ID' : f_id})
        f_id = argv['DeleteReservation_run_59']['f_id']
        c_id = argv['DeleteReservation_run_59']['c_id']
        F_SEATS_LEFT = state['TABLE_FLIGHT'].get({'F_ID' : c_id}, 'F_SEATS_LEFT')
        F_SEATS_LEFT = F_SEATS_LEFT + 1
        state['TABLE_FLIGHT'].update({'F_ID' : c_id}, {'F_SEATS_LEFT' : F_SEATS_LEFT})
        r_price = argv['DeleteReservation_run_59']['r_price']
        c_iattr00 = argv['DeleteReservation_run_59']['c_iattr00']
        c_iattr10 = argv['DeleteReservation_run_59']['c_iattr10']
        c_iattr11 = argv['DeleteReservation_run_59']['c_iattr11']
        c_id = argv['DeleteReservation_run_59']['c_id']
        C_BALANCE = state['TABLE_CUSTOMER'].get({'C_ID' : c_id}, 'C_BALANCE')
        C_IATTR00 = state['TABLE_CUSTOMER'].get({'C_ID' : c_id}, 'C_IATTR00')
        C_IATTR10 = state['TABLE_CUSTOMER'].get({'C_ID' : c_id}, 'C_IATTR10')
        C_IATTR11 = state['TABLE_CUSTOMER'].get({'C_ID' : c_id}, 'C_IATTR11')
        C_BALANCE = C_BALANCE - r_price
        C_IATTR00 = C_IATTR00 + c_iattr00
        C_IATTR10 = C_IATTR10 - c_iattr10
        C_IATTR11 = C_IATTR11 - c_iattr11
        state['TABLE_CUSTOMER'].update({'C_ID' : c_id}, {'C_BALANCE' : C_BALANCE,'C_IATTR00' : C_IATTR00,'C_IATTR10' : C_IATTR10,'C_IATTR11' : C_IATTR11})
        return state


    def cond1(self, state, argv):
        c_id = argv['DeleteReservation_run_59']['c_id']
        f_id = argv['DeleteReservation_run_59']['f_id']
        ff_al_id = argv['DeleteReservation_run_59']['ff_al_id']
        return And((Not(And (state['TABLE_CUSTOMER'].notNil({'C_ID' : c_id}),state['TABLE_CUSTOMER'].get({'C_ID' : c_id}, 'C_ID')== c_id) == False)),(Not(And (state['TABLE_FLIGHT'].notNil({'F_ID' : f_id}),state['TABLE_FLIGHT'].get({'F_ID' : f_id}, 'F_ID')== f_id) == False)),(Not(And (state['TABLE_RESERVATION'].notNil({'R_C_ID' : c_id,'R_F_ID' : f_id}),state['TABLE_RESERVATION'].get({'R_C_ID' : c_id,'R_F_ID' : f_id}, 'R_C_ID')== c_id,state['TABLE_RESERVATION'].get({'R_C_ID' : c_id,'R_F_ID' : f_id}, 'R_F_ID')== f_id) == False)))
    

    def csop1(self, state, argv):
        return True
    

    def sop1(self, state, argv):
        r_id = argv['DeleteReservation_run_59']['r_id']
        c_id = argv['DeleteReservation_run_59']['c_id']
        f_id = argv['DeleteReservation_run_59']['f_id']
        state['TABLE_RESERVATION'].delete({'R_ID' : r_id,'R_C_ID' : c_id,'R_F_ID' : f_id})
        f_id = argv['DeleteReservation_run_59']['f_id']
        c_id = argv['DeleteReservation_run_59']['c_id']
        F_SEATS_LEFT = state['TABLE_FLIGHT'].get({'F_ID' : c_id}, 'F_SEATS_LEFT')
        F_SEATS_LEFT = F_SEATS_LEFT + 1
        state['TABLE_FLIGHT'].update({'F_ID' : c_id}, {'F_SEATS_LEFT' : F_SEATS_LEFT})
        r_price = argv['DeleteReservation_run_59']['r_price']
        c_iattr00 = argv['DeleteReservation_run_59']['c_iattr00']
        c_iattr10 = argv['DeleteReservation_run_59']['c_iattr10']
        c_iattr11 = argv['DeleteReservation_run_59']['c_iattr11']
        c_id = argv['DeleteReservation_run_59']['c_id']
        C_BALANCE = state['TABLE_CUSTOMER'].get({'C_ID' : c_id}, 'C_BALANCE')
        C_IATTR00 = state['TABLE_CUSTOMER'].get({'C_ID' : c_id}, 'C_IATTR00')
        C_IATTR10 = state['TABLE_CUSTOMER'].get({'C_ID' : c_id}, 'C_IATTR10')
        C_IATTR11 = state['TABLE_CUSTOMER'].get({'C_ID' : c_id}, 'C_IATTR11')
        C_BALANCE = C_BALANCE - r_price
        C_IATTR00 = C_IATTR00 + c_iattr00
        C_IATTR10 = C_IATTR10 - c_iattr10
        C_IATTR11 = C_IATTR11 - c_iattr11
        state['TABLE_CUSTOMER'].update({'C_ID' : c_id}, {'C_BALANCE' : C_BALANCE,'C_IATTR00' : C_IATTR00,'C_IATTR10' : C_IATTR10,'C_IATTR11' : C_IATTR11})
        ff_itattr10 = argv['DeleteReservation_run_59']['ff_itattr10']
        c_id = argv['DeleteReservation_run_59']['c_id']
        ff_al_id = argv['DeleteReservation_run_59']['ff_al_id']
        FF_IATTR10 = state['TABLE_FREQUENT_FLYER'].get({'FF_C_ID' : c_id,'FF_AL_ID' : ff_al_id}, 'FF_IATTR10')
        FF_IATTR10 = FF_IATTR10 - ff_itattr10
        state['TABLE_FREQUENT_FLYER'].update({'FF_C_ID' : c_id,'FF_AL_ID' : ff_al_id}, {'FF_IATTR10' : FF_IATTR10})
        return state

class seats():
    def __init__(self):
        self.ops = [Op_UpdateReservation_run_84(), Op_UpdateCustomer_run_53(), Op_NewReservation_run_116(), Op_DeleteReservation_run_59()]
        self.tables = [AIRLINE,CONFIG_HISTOGRAMS,COUNTRY,AIRPORT,FLIGHT,RESERVATION,CONFIG_PROFILE,AIRPORT_DISTANCE,CUSTOMER,FREQUENT_FLYER]
        self.state = GenState
        self.argv = GenArgv
        self.axiom = BuildArgvAxiom(self.ops)

def factory():
    cls = globals()["seats"]
    return cls()

if __name__ == '__main__':
    check_parallel(factory, 8)
