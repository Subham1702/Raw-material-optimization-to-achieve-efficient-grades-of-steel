# Raw-material-optimization-to-achieve-efficient-grades-of-steel
## Project Description:
### Business Problem:
The steel manufacturing industry faces significant challenges in identifying optimal combination of raw materials and energy inputs necessary to produce high-quality steel efficiently.
### Business Objective: 
Maximize steel quality, Minimize costs.
### Business Constraint: 
Minimize energy use.
### Business Success Criteria: 
Reduce the processing time by 50%.
### Economic Success Criteria: 
Achieve a cost saving of at least $1M.
## Business Solution:
I gathered research papers and relevant datasets, then conducted Exploratory Data Analysis (EDA) on a client-provided secondary dataset using MySQL and Python to gain initial insights into steel production materials, cycle-time, and electricity consumption. Leveraging Auto-EDA libraries, I automated the EDA process, quickly generating comprehensive visualizations and statistical insights. After cleaning the data, I used Power BI and generated interactive dashboards.
## Dashboard 1: KPI.
![alt text](https://github.com/Subham1702/Raw-material-optimization-to-achieve-efficient-grades-of-steel/blob/main/Screenshot%20(368).png)

## Dashboard 2: Detailed Report.
![alt text](https://github.com/Subham1702/Raw-material-optimization-to-achieve-efficient-grades-of-steel/blob/main/Screenshot%20(367).png)

## Insights from the Data Analysis:
1. Correlation Matrix:
![alt text]()
- Scrap steel usage is positively correlated with yield increasing scrap steel leads to better production efficiency.
- Higher scrap steel usage shows a slight reduction in energy consumption making it more energy-efficient.
- Increasing the proportion of scrap steel can help optimize both yield and energy use
- Pig iron usage negatively correlates with yield meaning higher use reduces production efficiency.
- Increased pig iron usage slightly raises energy consumption driving up energy requirements.
- Total energy consumption strongly correlates with production costs, indicating that higher energy use leads to increased costs per ton.
2. Scatter Plot:
   (a). Scrap Steel (%) vs. Total Energy Consumption (Kwh): As the percentage of scrap steel increases, total energy consumption tends to decrease or remain stable. This suggests that increasing scrap steel usage could lead to more energy-efficient production, supporting the goal of minimizing energy consumption.
   (b). Pig Iron (%) vs. Estimated Cost per Ton ($): Higher percentages of pig iron result in higher estimated costs per ton. The plot shows a clear upward trend, meaning that reducing pig iron usage can help achieve cost savings, aligning with the business objective of reducing costs.

### Statistical Insights:
1. Correlation Analysis:
   - Scrap Steel (%) is positively correlated with Yield (%) and negatively correlated with Total Energy Consumption, meaning increased scrap steel usage improves yield and reduces energy consumption.
   - Pig Iron (%) is negatively correlated with Yield (%) and positively correlated with Estimated Cost per Ton. Higher pig iron usage increases production costs and lowers yield.
   - Total Energy Consumption is highly correlated with Cost per Ton, indicating that reducing energy consumption will directly reduce production costs.

2. Scatter Plots Analysis:
   - Increasing Scrap Steel usage leads to lower energy consumption, while higher Pig Iron usage increases costs.
   - Cost savings can be improved by optimizing the balance between scrap steel and pig iron.
  
### Business Insights:
1. Increase Scrap Steel Usage: This will help reduce energy consumption and increase yield, leading to cost savings.
2. Reduce Pig Iron Usage: Decreasing pig iron will lower production costs and increase efficiency.
3. Focus on Reducing Energy Consumption: Reducing energy usage, especially in energy-intensive stages, will help achieve the $1M cost-saving target.

## Recommendations:
- Optimize material composition to maximize yield and minimize costs.
- Focus on improving energy efficiency in the Electric Arc Furnace (EAF) and Ladle Refining Furnace (LRF) stages.




