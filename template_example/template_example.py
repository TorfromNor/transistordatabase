# imports
import numpy as np
import datetime
import sys
import os
from pymongo import MongoClient
from matplotlib import pyplot as plt
import json
import transistordatabase as tdb


# Template to generate a transistor
def Template():
    """
    * Initial author: N. Foerster
    * Date of creation: 8.2.2021
    * Last modified by: -
    * Date of modification: -
    * Version: 1.0.0
    * Compatibility: Python 3.9
    * Other files required:
    * Link to function:
    Syntax:


    Description:
    Template to generate a transistor object

    Input parameters:


    Output parameters:
     * Transistor

    Example:


    Known Bugs:


    """



    ####################################
    # transistor parameters
    ####################################
    # Create argument dictionaries
    transistor_args = {'name': 'CREE_C3M0016120K',
                       'type': 'SiC-MOSFET',
                       'author': 'Nikolas Förster',
                       'comment': '',
                       'manufacturer': 'Wolfspeed',
                       'datasheet_hyperlink': 'https://www.wolfspeed.com/downloads/dl/file/id/1483/product/0/c3m0016120k.pdf',
                       'datasheet_date': '2019-04',
                       'datasheet_version': "unknown",
                       'housing_area': 367e-6,
                       'cooling_area': 160e-6,
                       'housing_type': 'TO247',
                       'v_abs_max': 1200,
                       'i_abs_max': 250,
                       'i_cont': 115,
                       'c_iss':  {"t_j": 25, "graph_v_c": tdb.csv2array('transistor_c_iss.csv', first_x_to_0=True)},  # insert csv here
                       'c_oss': {"t_j": 25, "graph_v_c": tdb.csv2array('transistor_c_oss.csv', first_x_to_0=True)},  # insert csv here
                       'c_rss': {"t_j": 25, "graph_v_c": tdb.csv2array('transistor_c_rss.csv', first_x_to_0=True)},  # insert csv here
                       'graph_v_ecoss': tdb.csv2array('transistor_V_Eoss.csv'),
                       'r_g_int': 2.6,
                       'r_th_cs': 0,
                       'r_th_diode_cs': 0,
                       'r_th_switch_cs': 0,
                       }

    ####################################
    # switch parameters
    ####################################
    #### Metadata
    comment = "SiC switch"  # Optional
    manufacturer = "CREE"  # Optional
    technology = "unknown"  # Semiconductor technology. e.g. IGBT3/IGBT4/IGBT7  # Optional

    #### Channel parameters
    # channel data minus 40 degree
    channel_m40_15 = {"t_j": -40, 'v_g': 15,"graph_v_i": tdb.csv2array('switch_channel_m40_15V.csv', first_xy_to_00=True)}  # insert csv here
    channel_m40_13 = {"t_j": -40, 'v_g': 13, "graph_v_i": tdb.csv2array('switch_channel_m40_13V.csv', first_xy_to_00=True)}  # insert csv here
    channel_m4_11 = {"t_j": -40, 'v_g': 11, "graph_v_i": tdb.csv2array('switch_channel_m40_11V.csv', first_xy_to_00=True)}  # insert csv here
    channel_m40_9 = {"t_j": -40, 'v_g': 9, "graph_v_i": tdb.csv2array('switch_channel_m40_9V.csv', first_xy_to_00=True)}  # insert csv here
    channel_m40_7 = {"t_j": -40, 'v_g': 7, "graph_v_i": tdb.csv2array('switch_channel_m40_7V.csv', first_xy_to_00=True)}  # insert csv here
    # channel data 25 degree
    channel_25_15 = {"t_j": 25, 'v_g': 15,"graph_v_i": tdb.csv2array('switch_channel_25_15V.csv', first_xy_to_00=True)}  # insert csv here
    channel_25_13 = {"t_j": 25, 'v_g': 13, "graph_v_i": tdb.csv2array('switch_channel_25_13V.csv', first_xy_to_00=True)}  # insert csv here
    channel_25_11 = {"t_j": 25, 'v_g': 11, "graph_v_i": tdb.csv2array('switch_channel_25_11V.csv', first_xy_to_00=True)}  # insert csv here
    channel_25_9 = {"t_j": 25, 'v_g': 9, "graph_v_i": tdb.csv2array('switch_channel_25_9V.csv', first_xy_to_00=True)}  # insert csv here
    channel_25_7 = {"t_j": 25, 'v_g': 7, "graph_v_i": tdb.csv2array('switch_channel_25_7V.csv', first_xy_to_00=True)}  # insert csv here
    # channel data 175 degree
    channel_175_15 = {"t_j": 175, 'v_g': 15,"graph_v_i": tdb.csv2array('switch_channel_175_15V.csv', first_xy_to_00=True)}  # insert csv here
    channel_175_13 = {"t_j": 175, 'v_g': 13, "graph_v_i": tdb.csv2array('switch_channel_175_13V.csv', first_xy_to_00=True)}  # insert csv here
    channel_175_11 = {"t_j": 175, 'v_g': 11, "graph_v_i": tdb.csv2array('switch_channel_175_11V.csv', first_xy_to_00=True)}  # insert csv here
    channel_175_9 = {"t_j": 175, 'v_g': 9, "graph_v_i": tdb.csv2array('switch_channel_175_9V.csv', first_xy_to_00=True)}  # insert csv here
    channel_175_7 = {"t_j": 175, 'v_g': 7, "graph_v_i": tdb.csv2array('switch_channel_175_7V.csv', first_xy_to_00=True)}  # insert csv here

    #### switching parameters
    e_on_25_600 = {"dataset_type": "graph_i_e",
                   "t_j": 25,
                   'v_g': 15,
                   'v_supply': 600,
                   'r_g': 2.5,
                   "graph_i_e": tdb.csv2array('switch_switching_eon_2.5Ohm_600V_25deg_15V.csv')}  # insert csv here
    e_on_25_800 = {"dataset_type": "graph_i_e",
                   "t_j": 25,
                   'v_g': 15,
                   'v_supply': 800,
                   'r_g': 2.5,
                   "graph_i_e": tdb.csv2array('switch_switching_eon_2.5Ohm_800V_25deg_15V.csv')}  # insert csv here
    e_off_25_600 = {"dataset_type": "graph_i_e",
                   "t_j": 25,
                   'v_g': -4,
                   'v_supply': 600,
                   'r_g': 2.5,
                   "graph_i_e": tdb.csv2array('switch_switching_eoff_2.5Ohm_600V_25deg_-4V.csv')}  # insert csv here
    e_off_25_800 = {"dataset_type": "graph_i_e",
                    "t_j": 25,
                    'v_g': -4,
                    'v_supply': 800,
                    'r_g': 2.5,
                    "graph_i_e": tdb.csv2array('switch_switching_eoff_2.5Ohm_800V_25deg_-4V.csv')}  # insert csv here

    ### switch foster parameters
    switch_foster_args = {
        #'r_th_vector': r_th_vector,
        'r_th_total': 0.27,
        #'c_th_vector': c_th_vector,
        #'c_th_total': c_th_total,
        #'tau_vector': tau_vector,
        #'tau_total': tau_total,
        #'graph_t_rthjc': graph_t_rthjc
        }
    # switch_foster_args = None


    #### Bring the switch_args together
    switch_args = {
        'comment': comment,
        'manufacturer': manufacturer,
        'technology': technology,
        't_j_max': 175,
        'channel': [channel_m40_7, channel_m40_9, channel_m4_11, channel_m40_13, channel_m40_15, channel_25_15, channel_25_13, channel_25_11, channel_25_9, channel_25_7, channel_175_15, channel_175_13, channel_175_11, channel_175_9, channel_175_7],
        'e_on': [e_on_25_600, e_on_25_800],
        'e_off': [e_off_25_600, e_off_25_800],
        'thermal_foster': switch_foster_args}



    ####################################
    # diode parameters
    ####################################
    comment = 'comment diode'
    manufacturer = 'manufacturer diode'
    technology = 'technology diode'

    #### Channel parameters
    channel_25_0 = {"t_j": 25, 'v_g': 0, "graph_v_i": tdb.csv2array('diode_channel_25_0vgs.csv', first_xy_to_00=True, second_y_to_0=True)}  # insert csv here
    channel_25_neg2 = {"t_j": 25, 'v_g': -2, "graph_v_i": tdb.csv2array('diode_channel_25_-2vgs.csv', first_xy_to_00=True, second_y_to_0=True)}  # insert csv here
    channel_25_neg4 = {"t_j": 25, 'v_g': -4, "graph_v_i": tdb.csv2array('diode_channel_25_-4vgs.csv', first_xy_to_00=True, second_y_to_0=True)}  # insert csv here

    channel_175_0 = {"t_j": 175, 'v_g': 0, "graph_v_i": tdb.csv2array('diode_channel_175_0vgs.csv', first_xy_to_00=True, second_y_to_0=True)}  # insert csv here
    channel_175_neg2 = {"t_j": 175, 'v_g': -2, "graph_v_i": tdb.csv2array('diode_channel_175_-2vgs.csv', first_xy_to_00=True, second_y_to_0=True)}  # insert csv here
    channel_175_neg4 = {"t_j": 175, 'v_g': -4, "graph_v_i": tdb.csv2array('diode_channel_175_-4vgs.csv', first_xy_to_00=True, second_y_to_0=True)}  # insert csv here

    ### diode foster parameters
    diode_foster_args = {
        #'r_th_vector': r_th_vector,
        'r_th_total': 0,
        #'c_th_vector': c_th_vector,
        #'c_th_total': c_th_total,
        #'tau_vector': tau_vector,
        #'tau_total': tau_total,
        #'graph_t_rthjc': graph_t_rthjc
        }

    diode_args = {'comment': comment,
                  'manufacturer': manufacturer,
                  'technology': technology,
                  't_j_max': 175,
                  'channel': [channel_25_0, channel_25_neg2, channel_25_neg4, channel_175_0, channel_175_neg2, channel_175_neg4],
                  'e_rr': [],
                  'thermal_foster': diode_foster_args}

    ####################################
    # create transistor object
    ####################################
    return tdb.Transistor(transistor_args, switch_args, diode_args)

if __name__ == '__main__':
    
    transistor = Template()

    ####################################
    # Metadata
    ####################################

    print('---------------------')
    print("transistor metadata")
    print('---------------------')
    print(f"{transistor.name = }")
    print(f"{transistor.type = }")
    print(f"{transistor.author = }")
    print(f"{transistor.comment = }")
    print(f"{transistor.manufacturer = }")
    print(f"{transistor.datasheet_hyperlink = }")
    print(f"{transistor.datasheet_date = }")
    print(f"{transistor.datasheet_version = }")
    print(f"{transistor.housing_area = }")
    print(f"{transistor.cooling_area = }")
    print(f"{transistor.housing_type = }")
    print(f"{transistor.r_g_int = }")
    print('---------------------')
    print("switch metadata")
    print('---------------------')
    print(f"{transistor.switch.manufacturer = }")
    print(f"{transistor.switch.comment = }")
    print(f"{transistor.switch.technology = }")
    print(f"{transistor.switch.t_j_max = }")
    print('---------------------')
    print("diode metadata")
    print('---------------------')
    print(f"{transistor.diode.manufacturer = }")
    print(f"{transistor.diode.comment = }")
    print(f"{transistor.diode.technology = }")
    print(f"{transistor.diode.t_j_max = }")
    print('---------------------')
    print("working points")
    print('---------------------')
    # print(f"{transistor.wp.v_channel = }")
    # print(f"{transistor.wp.r_channel = }")
    # print(f"{transistor.wp.e_on = }")
    # print(f"{transistor.wp.e_off = }")
    # print(f"{transistor.wp.e_rr = }")
    ####################################
    # Method examples
    ####################################

    #### transistor methods ####
    transistor.wp.switch_v_channel, transistor.wp.switch_r_channel = transistor.calc_lin_channel(175, 15, 40, 'switch')  # linearisation at 175 degree, 15V gatevoltage, 40A channel current
    print(f"{transistor.wp.switch_v_channel = } V")
    print(f"{transistor.wp.switch_r_channel = } Ohm")
    # print(transistor.calc_v_eoss())
    # transistor.plot_v_eoss()
    # transistor.plot_v_qoss()
    # print(transistor.get_graph_v_i('switch', 25, 15))

    # print(transistor.get_graph_i_e('e_on', 25, 15, 600, 2.5))
    # print(transistor.get_graph_i_e('e_off', 25, -4, 600, 2.5))
    # print(transistor.get_graph_i_e('e_rr', 25, 15, 600, 2.5))  # not working in this example because of no e_rr for SiC-MOSFETs

    # export virtual datasheet as PDF
    # transistor.virtual_datasheet()

    #### switch methods ####
    # transistor.switch.plot_energy_data()
    # transistor.switch.plot_all_channel_data()
    # transistor.switch.plot_channel_data_vge(15)
    # transistor.switch.plot_channel_data_temp(175)


    #### diode methods ####
    # transistor.diode.plot_energy_data()
    # transistor.diode.plot_all_channel_data()

    ####################################
    # exporter example
    ####################################

    # Export to MATLAB

    # Export to SIMULINK

    # Export to geckoCIRCUITS
    tdb.export_geckocircuits(transistor, 600, 15, -4, 2.5, 2.5)

    ####################################
    # Database example
    ####################################
    # before init mongo, you need to install mongodb and start the database via the command line by using 'mongo' command
    # init mongodb
    # collection = tdb.Transistor.connect_local_TBD()  # Collection

    # reset the mongodb database
    # collection.drop()

    # store transistor
    # optional argument: collection. If no collection is specified, it connects to local TBD
    # transistor.save()

    # load transistor
    # optional argument: collection. If no collection is specified, it connects to local TBD
    transistor_loaded = tdb.Transistor.load({'name': 'CREE_C3M0016120K'})
    # print(transistor_loaded.switch.t_j_max)

    # export to json
    # optional argument: path. If no path is specified, saves exports to local folder
    # transistor_loaded.export_json()

    # import from json
    # optional argument: path. If no path is specified, it loads from to local folder
    # transistor_imported = Transistor.import_json('CREE_C3M0016120K.json')
    # print(transistor_imported.switch.t_j_max)

    # Transistor.connect_local_TBD().update_many({}, {"$rename": {"transistor_type": "type"}})








