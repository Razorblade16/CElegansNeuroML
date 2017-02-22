import c302
import sys

import neuroml.writers as writers


def setup(parameter_set,
          generate=False,
          duration=3000,
          dt=0.05,
          target_directory='examples',
          data_reader="UpdatedSpreadsheetDataReader"):
    
    exec ('from parameters_%s import ParameterisedModel' % parameter_set)
    params = ParameterisedModel()

    #params.set_bioparameter("unphysiological_offset_current", "0pA", "Testing TapWithdrawal", "0")
    params.set_bioparameter("unphysiological_offset_current_del", "0 ms", "Testing TapWithdrawal", "0")
    params.set_bioparameter("unphysiological_offset_current_dur", "2000 ms", "Testing TapWithdrawal", "0")

    cells = ['PLML', 'MDL01']
    #cells += ['AVAL']
    #cells += ['DB6']

    muscles_to_include = ['MDL01']

  
    cells_to_stimulate = ['PLML', 'MDL01']

    cells_to_plot = cells
    reference = "c302_%s_SingleMuscleTest" % parameter_set

    conn_polarity_override = {
      
    }

    conn_number_override = {
       
    }

    if generate:
        nml_doc = c302.generate(reference,
                                params,
                                cells=cells,
                                cells_to_plot=cells_to_plot,
                                cells_to_stimulate=cells_to_stimulate,
                                conn_polarity_override=conn_polarity_override,
                                conn_number_override=conn_number_override,
                                muscles_to_include=muscles_to_include,
                                duration=duration,
                                dt=dt,
                                target_directory=target_directory,
                                data_reader=data_reader)


    return cells, cells_to_stimulate, params, muscles_to_include


if __name__ == '__main__':
    parameter_set = sys.argv[1] if len(sys.argv) == 2 else 'C2'

    setup(parameter_set, generate=True, data_reader="UpdatedSpreadsheetDataReader")