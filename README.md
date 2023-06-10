# GrowthLysisDynam
The objective of this program is to process, analyze, and present optical density data from a Tecan K Microplate Reader. Optical density is a valuable tool in approximating and quantifying the generation of bacterial cells. This program serves as a method of further analyzing this data, allowing myself and other members of the You Lab to discover novel insights into bacterial growth dynamics.
This program consists of three main functions: Plotter, Growth, and Lysis. 
          
          Plotter: This program's task is to retrieve the optical density and time data from an Excel file, and display both
          graphically. The function also can be set to plot the natural log of the optical density. 
          
          Growth: This function takes the data of a specific strain as input, and returns the growth rate of that strain. 
          Bacterial growth is best approximated in the first four hours of incubation, thus the slope of the linear fit to the
          first four hours of data was used to estimate the growth rate.
          
          Lysis: Finally, the lysis function utilizes the growth function described previously and the proposed formula 
          for lysis as detailed in the paper cited below to return the lysis rate of a given strain of bacteria.
          
          
          
          
          
          
          
          
Citations:
"Robust, linear correlations between growth rates and beta-lactam-mediated lysis rates" ---------------------------------- Anna Lee et al.
