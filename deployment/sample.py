from bar import barGraph
from gender import genderPlot
from vaccination import vaccinationPlot
from map import mapPlot
import sys
import pandas as pd

if __name__ == "__main__":
    df = pd.read_csv(sys.argv[1])
    barGraph(df)
    genderPlot(df)
    vaccinationPlot(df)
    mapPlot(df)