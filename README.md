# Night-Sky-Brightness
Analyzing data about light pollution across the globe


I utilized three months of data collected by the Globe at Night Sky Brightness Monitoring Network to compare the level of light pollution across different locations. This was measured as a Night Sky Brightness (NSB) value.  In total, this amounted to over 4 million individual data entries. 

My original intent was to find the ten brightest locations for each month (July, August, and September of 2020) and compare the three months to determine the amount of variance across that time frame.  However, as I began to filter the results I realized that many locations didn’t report results all three months and comparing the results of the months wouldn’t show me very much because I would be looking at different locations.  Instead, I added code that filtered the locations down to only those who reported all three months.  This gave me 20 locations instead of 10. Since it was a nice, round number I decided to include all twenty.

I used Tkinter to create a GUI that displayed a simple bar graph showing the average NSB of each location for each individual month. I used the locations as the x-axis and the NSB value as the y-axis.  When clicked, these also print a list of the locations with their average NSB in the console. Additionally, I added a fourth grouped bar chart to show all the data in one chart.  This was especially tricky and took me forever to get right.	

Overall,	the data was about what I expected. There was not a huge amount variance among the locations. There were certain locations that reported much higher NSBs and there was some variance month to month, but mostly they were consistent.  What this data doesn’t tell me is what accounts for the higher or lower NSB values across the locations.
