SELECT count(*) FROM `Covid-19`.OWID_Daily;

select * from OWID_Daily as a 
where a.`date` = "2021-03-22"
and a.`location` in ("United Kingdom", "France");

select `date`, a.`location`, a.`total_deaths_per_million` from  OWID_Daily as a 
inner join 
(select `location`, max(`date`) as maxdate from OWID_Daily group by `location`) as c
on a.`date` = c.maxdate and a.`location` = c.`location`;


select `location`, max(`date`) as maxdate from OWID_Daily as b group by `location`;