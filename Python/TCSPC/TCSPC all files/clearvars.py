def clearvars(skipvars):
    var = None
    delnames = []
    skipvars.append('var')
    skipvars.append('delnames')
    skipvars.append('skipvars')
    skipvars.append('i')
    
    for var in vars():
        if var not in skipvars and var[0] != '_': #always skip the auto variables
            delnames.append(var)
    for i in range(len(delnames)):
        exec('del ' + delnames[i])
    del var

    #del delnames #you may want to keep these around to remember what you skipped/kept
    #del skipvars

skipvars = ['LoadSkip', 'DoParam', 'PathD', 'ResetPlot', 'DefaultFigSize', 'DefaultFigColour', 'DefaultFigPosn', 'isSaveFigs']

