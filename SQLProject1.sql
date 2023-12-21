##### 1) #####
Select *
From PortfolioProject..CovidDeaths$
Where continent is not null
order by 3, 4

##### 2) #####
-- Selects Data that we are going to be using
	
Select Location, date, total_cases, new_cases, total_deaths, population
From PortfolioProject.. CovidDeaths$
order by 1,2

##### 3) #####
-- Looking at Total Cases vs Total Deaths
-- Shows likelihood of dying if you contract covid in your country
	
SELECT Location, date, total_cases,total_deaths,CASE 
WHEN total_cases = 0 THEN 0 -- To handle division by zero
ELSE (CAST(total_deaths AS FLOAT) / total_cases) * 100 
END AS DeathPercentage
FROM PortfolioProject..CovidDeaths$
ORDER BY 1, 2;

##### 4) #####
-- Looking at Total Cases vs Population
-- Shows what percentage of population has gotten Covid

Select Location, date, Population, total_cases, (total_cases/population)*100 as PercentPopulationInfected
From PortfolioProject..CovidDeaths$
Where location like '%states%'
order by 1,2

##### 5) #####
-- Looking at countries with highest infection rate compared to population
	
Select Location, Population, MAX(total_cases) as HighestInfectionCount, MAX((total_cases/population))*100 as PercentPopulationInfected
From PortfolioProject..CovidDeaths$
--Where location like '%states%'
Group by Location, population
order by PercentPopulationInfected desc

##### 6) #####
-- This is showing countries with the highest Death Count per Population

Select Location, MAX(cast(total_deaths as int)) as TotalDeathCount
From PortfolioProject..CovidDeaths$
--Where location like '%states%'
Where continent is not null
Group by Location, population
order by TotalDeathCount desc

##### 7) #####
-- This breaks things down by continent
-- Showing continents with the highest death count per population

Select continent, MAX(cast(total_deaths as int)) as TotalDeathCount
From PortfolioProject..CovidDeaths$
--Where location like '%states%'
Where continent is not null
Group by continent
order by TotalDeathCount desc

##### 8) #####
-- GLOBAL NUMBERS

SELECT date, SUM(new_cases) as total_cases, SUM(ISNULL(cast(new_deaths as int), 0)) as total_deaths, SUM(ISNULL(cast(new_deaths as int), 0)) / NULLIF(SUM(New_Cases), 0) * 100 as DeathPercentage
FROM PortfolioProject..CovidDeaths$
--Where location like '%states%'
WHERE continent is not null
GROUP BY date
ORDER BY 1, 2;

##### 9) #####
-- Looking at Total Population vs Vaccinations

Select dea.continent, dea.location, dea.date, dea.population, vac.new_vaccinations
, SUM(ISNULL(CONVERT(BIGINT,vac.new_vaccinations), 0)) OVER (Partition by dea.location Order by dea.location, dea.date) as RollingPeopleVaccinated
--, (RollingPeopleVaccinated/population)*100
From PortfolioProject..CovidDeaths$ dea
Join PortfolioProject..CovidVaccinations$ vac
	On dea.location = vac.location
	and dea.date = vac.date
WHERE dea.continent is not null
ORDER BY 2, 3;

##### 10) #####
-- Use CTE 

With PopvsVac (Continent, Location, Date, Population, New_Vaccinations, RollingPeopleVaccinated)
as
(
Select dea.continent, dea.location, dea.date, dea.population, vac.new_vaccinations
, SUM(ISNULL(CONVERT(BIGINT,vac.new_vaccinations), 0)) OVER (Partition by dea.location Order by dea.location, dea.date) as RollingPeopleVaccinated
--, (RollingPeopleVaccinated/population)*100
From PortfolioProject..CovidDeaths$ dea
Join PortfolioProject..CovidVaccinations$ vac
	On dea.location = vac.location
	and dea.date = vac.date
WHERE dea.continent is not null
--ORDER BY 2, 3;
)
Select*, (RollingPeopleVaccinated/Population)*100
From PopvsVac

##### 11) #####
-- TEMP TABLE

Drop Table if exists #PercentPopulationVaccinated  --This will drop the previous table created before running the query if you make changes
Create Table #PercentPopulationVaccinated
(
Continent nvarchar (255),
Location nvarchar (255),
Date datetime,
Population numeric,
New_Vaccinations numeric,
RollingPeopleVaccinated numeric
)

Insert into #PercentPopulationVaccinated
Select dea.continent, dea.location, dea.date, dea.population, vac.new_vaccinations
, SUM(ISNULL(CONVERT(BIGINT,vac.new_vaccinations), 0)) OVER (Partition by dea.location Order by dea.location, dea.date) as RollingPeopleVaccinated
--, (RollingPeopleVaccinated/population)*100
From PortfolioProject..CovidDeaths$ dea
Join PortfolioProject..CovidVaccinations$ vac
	On dea.location = vac.location
	and dea.date = vac.date
WHERE dea.continent is not null
--ORDER BY 2, 3

Select*, (RollingPeopleVaccinated/Population)*100
From #PercentPopulationVaccinated

##### 12) #####
--Creating View to store data for later visulizations

Create View PercentPopulationVaccinated as 
Select dea.continent, dea.location, dea.date, dea.population, vac.new_vaccinations
, SUM(ISNULL(CONVERT(BIGINT,vac.new_vaccinations), 0)) OVER (Partition by dea.location Order by dea.location, dea.date) as RollingPeopleVaccinated
--, (RollingPeopleVaccinated/population)*100
From PortfolioProject..CovidDeaths$ dea
Join PortfolioProject..CovidVaccinations$ vac
	On dea.location = vac.location
	and dea.date = vac.date
WHERE dea.continent is not null
--ORDER BY 2, 3

Select *
From PercentPopulationVaccinated
