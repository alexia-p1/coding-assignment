cd "C:\Users\Popa_Alexia\Documents\coding for economists" 
use "data\hotels-vienna.csv", clear

foreach var of varlist city_actual price stars distance accommodation_type rating {
    count if missing(`var') 
    di "Variable `var' has " r(N) " missing observations."
}

generate distcat=1 if distance<1 /*close to the city centre*/
replace distcat=2 if distance>=1 /*far from the city centre*/

tabstat price stars rating, by(distcat) stat(mean sd min max)

scatter price distance || lfit price distance
graph export "C:\Users\Popa_Alexia\Documents\coding for economists\coding assignment\Graph.pdf", as(pdf) name("Graph")

save "coding assignment\hotels-vienna.dta", replace