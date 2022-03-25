# Script para realizar a interpolação por Krigagem

#Instalado pacotes
#install.packages("maptools")

#Importando bibliotecas
library(sp)       
library(maptools) 
library(raster)   
library(gstat)  
library(graphics)
library(lattice)


# Selecionando área de trabalho
setwd("D:\\tmg\\sprint-3")

# DataFrames
#df_argila_convertido
#df_argila_filtrado_outliers
#df_argila_filtrado_opcao_1
#df_argila_filtrado_opcao_5


#Lendo arquivo de dados
dados <- read.csv('dados/solo/dados_caracteristica/argila/df_argila_convertido.csv')
coordinates(dados) <- ~x+y
head(dados)

#Lendo contorno do estado do Paraná
coords <- read.csv('dados/solo/contornos/contorno_parana.csv')
coordinates(coords) = ~x+y 
contorno = SpatialPolygons( list(Polygons(list(Polygon(coords)), 1)))
plot(contorno)

#Inicio da Análise dos semivariogramas
variograma <- variogram(Argila~1, dados)

#Plotando o Variografico 
plot(variograma,pch=16,col=1)  #pch: Formato - Col: Cores

# Modelo esférico
modelo.sph <- fit.variogram(object = variograma, model=vgm(psill = 50000, nugget = 20000, range = 150000, model = "Sph"))
(sqr.E<-attr(modelo.sph, "SSErr"))

#Plotando semivariograma esférico
plot(variograma,model=modelo.sph, col=1,pl=F,pch=16,xlab="Distância",ylab="Semivariância",
     main =" Semivariograma - Modelo Esférico ")

# Modelo Gaussiano
modelo.gau <- fit.variogram(object = variograma, model=vgm(psill = 50000, nugget = 20000, range = 150000, model = "Gau"))
(sqr.E<-attr(modelo.gau, "SSErr"))

#Plotando semivariograma Gaussiano
plot(variograma,model=modelo.gau, col=1,pl=F,pch=16,xlab="Distância",ylab="Semivariância",
     main =" Semivariograma - Modelo Gaussiano")

# Modelo Exponencial
modelo.exp <- fit.variogram(object = variograma, model=vgm(psill = 50000, nugget = 20000, range = 150000, model = "Exp"))
(sqr.E<-attr(modelo.exp, "SSErr"))

#Plotando semivariograma exponencial
plot(variograma,model=modelo.exp, col=1,pl=F,pch=16,xlab="Distância",ylab="Semivariância",
     main =" Semivariograma - Modelo Exponencial ")



#Criando o grid 
x<-coords$x
y<-coords$y
dis <- 1000 #Distância entre pontos
grid <- expand.grid(X=seq(min(x),max(x),dis), Y=seq(min(y),max(y),dis))
gridded(grid) = ~ X + Y
plot(grid)

#Realizando a Krigagem 
ko.argila <- krige(Argila~1, dados, grid,modelo.sph)
ko.argila <- as.data.frame(ko.argila)
coordinates(ko.argila)=~X+Y 
gridded(ko.argila)=TRUE 
ko.argila <- raster(ko.argila) 
plot(ko.argila)

 #Recortando com o contorno
ko.argila <- mask(ko.argila, contorno, inverse=FALSE)
x11()
plot(ko.argila, xlab="X (UTM)",ylab="Y (UTM)",  xlim = c(100000, 800000), ylim = c(7000000, 7600000),
     main =" Argila - Paraná ")
plot(contorno, add=T)
contour(ko.argila, add=T, nlevels = 6)

