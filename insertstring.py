
def getparams(id, valuelist):
    try:
          params = [id]
          for i in range (len(valuelist)):
                if valuelist[i] != "":
                      params.append(valuelist[i])

    except Exception as e:
        pass

    return params


def getinsertstring(valuelist):
    try:
      param_markers = "%s"
      insert_string = "INSERT INTO `Covid-19`.`OWID_Daily` "
      insert_string += "(`id` "
      if valuelist[0] != "": insert_string += ", `iso_code` " ; param_markers += ", %s"
      if valuelist[1] != "": insert_string += ", `continent`" ; param_markers += ", %s"
      if valuelist[2] != "": insert_string += ", `location`" ; param_markers += ", %s"
      if valuelist[3] != "": insert_string += ", `date`" ; param_markers += ", %s"
      if valuelist[4] != "": insert_string += ", `total_cases`" ; param_markers += ", %s"
      if valuelist[5] != "": insert_string += ", `new_cases`" ; param_markers += ", %s"
      if valuelist[6] != "": insert_string += ", `new_cases_smoothed`" ; param_markers += ", %s"
      if valuelist[7] != "": insert_string += ", `total_deaths`" ; param_markers += ", %s"
      if valuelist[8] != "": insert_string += ", `new_deaths`" ; param_markers += ", %s"
      if valuelist[9] != "": insert_string += ", `new_deaths_smoothed`" ; param_markers += ", %s"
      if valuelist[10] != "": insert_string += ", `total_cases_per_million`" ; param_markers += ", %s"
      if valuelist[11] != "": insert_string += ", `new_cases_per_million`" ; param_markers += ", %s"
      if valuelist[12] != "": insert_string += ", `new_cases_smoothed_per_million`" ; param_markers += ", %s"
      if valuelist[13] != "": insert_string += ", `total_deaths_per_million`" ; param_markers += ", %s"
      if valuelist[14] != "": insert_string += ", `new_deaths_per_million`" ; param_markers += ", %s"
      if valuelist[15] != "": insert_string += ", `new_deaths_smoothed_per_million`" ; param_markers += ", %s"
      if valuelist[16] != "": insert_string += ", `reproduction_rate`" ; param_markers += ", %s"
      if valuelist[17] != "": insert_string += ", `icu_patients`" ; param_markers += ", %s"
      if valuelist[18] != "": insert_string += ", `icu_patients_per_million`" ; param_markers += ", %s"
      if valuelist[19] != "": insert_string += ", `hosp_patients`" ; param_markers += ", %s"
      if valuelist[20] != "": insert_string += ", `hosp_patients_per_million`" ; param_markers += ", %s"
      if valuelist[21] != "": insert_string += ", `weekly_icu_admissions`" ; param_markers += ", %s"
      if valuelist[22] != "": insert_string += ", `weekly_icu_admissions_per_million`" ; param_markers += ", %s"
      if valuelist[23] != "": insert_string += ", `weekly_hosp_admissions`" ; param_markers += ", %s"
      if valuelist[24] != "": insert_string += ", `weekly_hosp_admissions_per_million`" ; param_markers += ", %s"
      if valuelist[25] != "": insert_string += ", `new_tests`" ; param_markers += ", %s"
      if valuelist[26] != "": insert_string += ", `total_tests`" ; param_markers += ", %s"
      if valuelist[27] != "": insert_string += ", `total_tests_per_thousand`" ; param_markers += ", %s"
      if valuelist[28] != "": insert_string += ", `new_tests_per_thousand`" ; param_markers += ", %s"
      if valuelist[29] != "": insert_string += ", `new_tests_smoothed`" ; param_markers += ", %s"
      if valuelist[30] != "": insert_string += ", `new_tests_smoothed_per_thousand`" ; param_markers += ", %s"
      if valuelist[31] != "": insert_string += ", `positive_rate`" ; param_markers += ", %s"
      if valuelist[32] != "": insert_string += ", `tests_per_case`" ; param_markers += ", %s"
      if valuelist[33] != "": insert_string += ", `tests_units`" ; param_markers += ", %s"
      if valuelist[34] != "": insert_string += ", `total_vaccinations`" ; param_markers += ", %s"
      if valuelist[35] != "": insert_string += ", `people_vaccinated`" ; param_markers += ", %s"
      if valuelist[36] != "": insert_string += ", `people_fully_vaccinated`" ; param_markers += ", %s"
      if valuelist[37] != "": insert_string += ", `new_vaccinations`" ; param_markers += ", %s"
      if valuelist[38] != "": insert_string += ", `new_vaccinations_smoothed`" ; param_markers += ", %s"
      if valuelist[39] != "": insert_string += ", `total_vaccinations_per_hundred`" ; param_markers += ", %s"
      if valuelist[40] != "": insert_string += ", `people_vaccinated_per_hundred`" ; param_markers += ", %s"
      if valuelist[41] != "": insert_string += ", `people_fully_vaccinated_per_hundred`" ; param_markers += ", %s"
      if valuelist[42] != "": insert_string += ", `new_vaccinations_smoothed_per_million`" ; param_markers += ", %s"
      if valuelist[43] != "": insert_string += ", `stringency_index`" ; param_markers += ", %s"
      if valuelist[44] != "": insert_string += ", `population`" ; param_markers += ", %s"
      if valuelist[45] != "": insert_string += ", `population_density`" ; param_markers += ", %s"
      if valuelist[46] != "": insert_string += ", `median_age`" ; param_markers += ", %s"
      if valuelist[47] != "": insert_string += ", `aged_65_older`" ; param_markers += ", %s"
      if valuelist[48] != "": insert_string += ", `aged_70_older`" ; param_markers += ", %s"
      if valuelist[49] != "": insert_string += ", `gdp_per_capita`" ; param_markers += ", %s"
      if valuelist[50] != "": insert_string += ", `extreme_poverty`" ; param_markers += ", %s"
      if valuelist[51] != "": insert_string += ", `cardiovasc_death_rate`" ; param_markers += ", %s"
      if valuelist[52] != "": insert_string += ", `diabetes_prevalence`" ; param_markers += ", %s"
      if valuelist[53] != "": insert_string += ", `female_smokers`" ; param_markers += ", %s"
      if valuelist[54] != "": insert_string += ", `male_smokers`" ; param_markers += ", %s"
      if valuelist[55] != "": insert_string += ", `handwashing_facilities`" ; param_markers += ", %s"
      if valuelist[56] != "": insert_string += ", `hospital_beds_per_thousand`" ; param_markers += ", %s"
      if valuelist[57] != "": insert_string += ", `life_expectancy`" ; param_markers += ", %s"
      if valuelist[58] != "": insert_string += ", `human_development_index`" ; param_markers += ", %s"
      insert_string += ") VALUES  ( " + param_markers + " );"
    except Exception as e:
        pass

    return insert_string