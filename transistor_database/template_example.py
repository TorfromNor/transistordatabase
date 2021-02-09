# imports
from databaseClasses import Transistor
from databaseClasses import csv2array
import numpy as np
import datetime

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
    name = 'CREE_C3M0016120K'
    transistor_type = 'SiC-MOSFET'
    v_max = 1200
    i_max = 250
    i_cont = 115

    # Create argument dictionaries
    transistor_args = {'name': name, 'transistor_type': transistor_type, 'v_max': v_max,
                       'i_max': i_max, 'i_cont': i_cont}
    ####################################
    # metadata parameters
    ####################################
    # ToDo: use SI-based things. No mJ, no mJ, ...

    author = 'Nikolas Foerster'
    comment = ''
    manufacturer = 'Wolfspeed'
    datasheet_hyperlink = 'https://www.wolfspeed.com/downloads/dl/file/id/1483/product/0/c3m0016120k.pdf'
    datasheet_date = '2019-04'
    datasheet_version = "unknown"
    housing_area = 367e-6
    cooling_area = 160e-6
    housing_type = 'TO247'

    metadata_args = {'author': author, 'comment': comment, 'manufacturer': manufacturer,
                     'datasheet_hyperlink': datasheet_hyperlink, 'datasheet_date': datasheet_date,
                     'datasheet_version': datasheet_version, 'housing_area': housing_area,
                     'cooling_area': cooling_area, 'housing_type': housing_type}



    ####################################
    # switch parameters
    ####################################
    #### Metadata
    comment = "SiC switch"  # Optional
    manufacturer = "CREE"  # Optional
    technology = "unknown" # Semiconductor technology. e.g. IGBT3/IGBT4/IGBT7  # Optional

    # Constant Capacitances
    c_oss = 5   # Unit: pF  # Optional
    c_iss = 3  # Unit: pF  # Optional
    c_rss = 4    # Unit: pF  # Optional

    #### Channel parameters
    # channel data 25 degree
    channel_25_15 = {"t_j": 25, 'v_g': 15,"v_i_data": csv2array('switch_channel_25_vg15.csv', True, True)}  # insert csv here
    channel_25_13 = {"t_j": 25, 'v_g': 13, "v_i_data": csv2array('switch_channel_25_vg13.csv', True, True)}  # insert csv here
    channel_25_11 = {"t_j": 25, 'v_g': 11, "v_i_data": csv2array('switch_channel_25_vg11.csv', True, True)}  # insert csv here
    channel_25_9 = {"t_j": 25, 'v_g': 9, "v_i_data": csv2array('switch_channel_25_vg9.csv', True, True)}  # insert csv here
    channel_25_7 = {"t_j": 25, 'v_g': 7, "v_i_data": csv2array('switch_channel_25_vg7.csv', True, True)}  # insert csv here
    # channel data 175 degree
    channel_175_15 = {"t_j": 175, 'v_g': 15,"v_i_data": csv2array('switch_channel_175_vg15.csv', True, True)}  # insert csv here
    channel_175_13 = {"t_j": 175, 'v_g': 13, "v_i_data": csv2array('switch_channel_175_vg13.csv', True, True)}  # insert csv here
    channel_175_11 = {"t_j": 175, 'v_g': 11, "v_i_data": csv2array('switch_channel_175_vg11.csv', True, True)}  # insert csv here
    channel_175_9 = {"t_j": 175, 'v_g': 9, "v_i_data": csv2array('switch_channel_175_vg9.csv', True, True)}  # insert csv here
    channel_175_7 = {"t_j": 175, 'v_g': 7, "v_i_data": csv2array('switch_channel_175_vg7.csv', True, True)}  # insert csv here


   # print(csv2array('switch_switching_eon_2.5Ohm_600V_25deg_15V.csv', False))
    print(np.shape(csv2array('switch_switching_eon_2.5Ohm_600V_25deg_15V.csv', False, False)))

    #### switching parameters
    e_on_25_600 = {"dataset_type": "graph_i_e",
                   "t_j": 25,
                   'v_g': 15,
                   'v_supply': 600,
                   'r_g': 2.5,
                   "i_e_data": csv2array('switch_switching_eon_2.5Ohm_600V_25deg_15V.csv', False, False)}  # insert csv here
    e_on_25_800 = {"dataset_type": "graph_i_e",
                   "t_j": 25,
                   'v_g': 15,
                   'v_supply': 600,
                   'r_g': 2.5,
                   "i_e_data": csv2array('switch_switching_eon_2.5Ohm_800V_25deg_15V.csv', False, False)}  # insert csv here
    e_off_25_600 = {"dataset_type": "graph_i_e",
                   "t_j": 25,
                   'v_g': -4,
                   'v_supply': 600,
                   'r_g': 2.5,
                   "i_e_data": csv2array('switch_switching_eoff_2.5Ohm_600V_25deg_-4V.csv', False, False)}  # insert csv here
    e_off_25_800 = {"dataset_type": "graph_i_e",
                    "t_j": 25,
                    'v_g': -4,
                    'v_supply': 600,
                    'r_g': 2.5,
                    "i_e_data": csv2array('switch_switching_eoff_2.5Ohm_800V_25deg_-4V.csv', False, False)}  # insert csv here

    #### Bring the switch_args together
    switch_args = {
        'comment': comment,
        'manufacturer': manufacturer,
        'technology': technology,
        'c_oss': c_oss,
        'c_iss': c_iss,
        'c_rss': c_rss,
        'channel': [channel_25_15, channel_25_13, channel_25_11, channel_25_9, channel_25_7, channel_175_15, channel_175_13, channel_175_11, channel_175_9, channel_175_7],
        'e_on': [e_on_25_600, e_on_25_800],
        'e_off': [e_off_25_600, e_off_25_800]}

    ####################################
    # switch foster parameters
    ####################################
    #
    # foster_args = {'r_th_vector': r_th_vector, 'r_th_total': r_th_total, 'c_th_vector': c_th_vector,
    #                'c_th_total': c_th_total, 'tau_vector': tau_vector, 'tau_total': tau_total,
    #                'transient_data': transient_data}
    foster_args = None

    ####################################
    # diode parameters
    ####################################
    comment = ''
    manufacturer = 'unknown'
    technology = ''

    #### Channel parameters
    channel_25_0 = {"t_j": 25, 'v_g': 0, "v_i_data": csv2array('diode_channel_25_0vgs.csv', True, True)}  # insert csv here
    channel_25_neg2 = {"t_j": 25, 'v_g': -2, "v_i_data": csv2array('diode_channel_25_-2vgs.csv', True, True)}  # insert csv here
    channel_25_neg4 = {"t_j": 25, 'v_g': -4, "v_i_data": csv2array('diode_channel_25_-4vgs.csv', True, True)}  # insert csv here

    channel_175_0 = {"t_j": 25, 'v_g': 0, "v_i_data": csv2array('diode_channel_175_0vgs.csv', True, True)}  # insert csv here
    channel_175_neg2 = {"t_j": 25, 'v_g': -2, "v_i_data": csv2array('diode_channel_175_-2vgs.csv', True, True)}  # insert csv here
    channel_175_neg4 = {"t_j": 25, 'v_g': -4, "v_i_data": csv2array('diode_channel_175_-4vgs.csv', True, True)}  # insert csv here



    diode_args = {'comment': comment,
                  'manufacturer': manufacturer,
                  'technology': technology,
                  'channel': [channel_25_0, channel_25_neg2, channel_25_neg4, channel_175_0, channel_175_neg2, channel_175_neg4],
                  'e_rr': []}


    ####################################
    # diode foster parameters
    ####################################
    # ToDo:

    ####################################
    # create transistor object
    ####################################
    # Create transistor object
    return Transistor(transistor_args, metadata_args, foster_args, switch_args, diode_args)

if __name__ == '__main__':
    transistor = Template()

    print(transistor.name)
    print(transistor.switch.manufacturer)
    print(transistor.switch.channel[0].v_i_data)

    # ToDo: store transistor in database