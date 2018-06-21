# install.packages("DMwR")
# install.packages("pROC")
# install.packages('caret')
# install.packages('ggplot2')
# install.packages('pROC')
# install.packages("randomForest")
# install.packages("rpart")
# install.packages("e1071")
# instal.pacakges("klaR")
# install.packages("RWeka")
# install.packages('ggdentro')
# install.packages('protoclust')
# install.packages('knitr')
# install.packages('dplry')
library(RWeka)
library(klaR)
library(rpart)
library(e1071)
library(randomForest)
library(pROC)
library(DMwR)
library(ggplot2)
library(caret)


setwd("D:/Universidad/PDG/Feature extraction")
dataset_final <- read.table("Final.csv",sep = ";", fill = TRUE ,header = TRUE)

benignas <- read.table("testNormal.csv",sep = ";", fill = TRUE ,header = TRUE)
malignas <- read.table("testMalicioso.csv",sep = ";", fill = TRUE ,header = TRUE)



test_data <- read.table("FinalTesting.csv", sep= ";", fill=TRUE, header = TRUE)
test_data <- read.table("testMalicioso.csv", sep= ";", fill=TRUE, header = TRUE)

test_data <- test_data[,-c(1,18)]

summary(dataset_final$attack_type)
summary(dataset_final$type)

ggplot(dataset_final,aes(x=dataset_final$type, fill = dataset_final$type)) + geom_bar() +labs(x="TIPO",y="CANTIDAD")
ggplot(dataset_final,aes(x=dataset_final$attack_type,fill = dataset_final$attack_type))+geom_bar() +labs(x="TIPO",y="CANTIDAD")




dataset_final <- dataset_final[,c(-1,-18)]
malignas <- malignas[,c(-1,-18)]
#dataset_final <- read.table("final_dataset.csv",sep = ";", fill = TRUE ,header = TRUE)
summary(malignas)


#Mirando proporcion del dataset
str(dataset_final)
summary(dataset_final)
table(dataset_final$type)
length(unique(dataset_final$npcap))


#Particionamiento del dataset para training y test
set.seed(1234)
splitIndex <- createDataPartition(dataset_final$type, p = .70,
                                  list = FALSE,
                                  times = 1)
trainSplit <- dataset_final[ splitIndex,]
testSplit <- dataset_final[-splitIndex,]




modelos<-matrix(c(prop.table(table(dataset_final$type))[1],"-","-",0,0,0,0,0,0,0,0,0,0,0,0),ncol=3,byrow=TRUE)
colnames(modelos)<-c("Accuaracy", "Kappa", "F Score")
rownames(modelos)<-c("Baseline","Random Forest", "KNN","C 4.5","Naïve Bayes")
modelos<-as.table(modelos)
modelos


############################# METODOS DE CLASIFICACION ##############################
## Método de entrenamiento - K-fold CrossValidation 
trControlCv <- trainControl(method="cv", number=10)


##########RANDOM FOREST##########

set.seed(54321)

#Entrenamiento del modelo
rForest <- train(type~., data  = dataset_final, method = "rf", 
                      trControl = trControlCv)

#Modelo final
rForest

#Validacion del modelo
#prediccionesRforestB<-predict(rForest,newdata=benignas)
prediccionesRforestM<-predict(rForest,newdata=test_data)

#confusionMatrix(prediccionesRforestB,benignas$type)
cMatrixRForest <-confusionMatrix(prediccionesRforestM,test_data$type)
cMatrixRForest
summary(test_data)
modelos[2,1]<-as.numeric(cMatrixRForest$overall[1])
modelos[2,2]<-as.numeric(cMatrixRForest$overall[2])
modelos[2,3]<-as.numeric(cMatrixRForest$byClass[7])

########## KNN ##########
set.seed(9999)

#Entrenamiento del modelo
knn_model <- train(type~., data = dataset_final, method = "knn", trControl = trControlCv)

#Modelo
knn_model

#Validacion del modelo
prediccionesKnn <- predict(knn_model, newdata=test_data)
cMatrixKnn <- confusionMatrix(prediccionesKnn,test_data$type)
modelos[3,1]<-as.numeric(cMatrixKnn$overall[1])
modelos[3,2]<-as.numeric(cMatrixKnn$overall[2])
modelos[3,3]<-as.numeric(cMatrixKnn$byClass[7])



##########C 4.5##########

set.seed(9876)

#Entrenamineto del modelo
c4_5<-J48(type~.,data=dataset_final)
#evaluate_Weka_classifier(c4_5,numFolds = 10,class = TRUE,seed = 4567)

#Modelo
c4_5
summary(c4_5)

#Validacion del modelo
prediccionesC4_5<- predict(c4_5, test_data)
cMatrixC4_5 <- confusionMatrix(prediccionesC4_5,test_data$type)
modelos[4,1]<-as.numeric(cMatrixC4_5$overall[1])
modelos[4,2]<-as.numeric(cMatrixC4_5$overall[2])
modelos[4,3]<-as.numeric(cMatrixC4_5$byClass[7])


########## Naïve Bayes ##########
set.seed(4444)

#Entrenamiento del modelo
modelo_nb <- train(type~., data  = dataset_final, method = "nb", 
                   trControl = trControlCv)

#Modelo
modelo_nb

#Validacion del modelo
prediccionesNb <- predict(modelo_nb, test_data)
cMatrixNb <- confusionMatrix(prediccionesNb,test_data$type)
modelos[5,1]<-as.numeric(cMatrixNb$overall[1])
modelos[5,2]<-as.numeric(cMatrixNb$overall[2])
modelos[5,3]<-as.numeric(cMatrixNb$byClass[7])



##############################Comparación modelos############################
comparacionModelos<-as.data.frame.matrix(modelos)
comparacionModelos
