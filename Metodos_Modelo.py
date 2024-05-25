
# Librerias

from sklearn.metrics import (mean_squared_error, r2_score, 
	mean_absolute_error, confusion_matrix, recall_score, precision_score,
	f1_score, accuracy_score, classification_report)

class MetodosParaModelos:

	def entrenamiento(self, modelo, X_train, y_train):
		modelo.fit(X_train, y_train)		

	def metricas_regresion(self, y_test, y_hat):
		print(f'MSE: {mean_squared_error(y_test, y_hat)}')
		print(f'R2: {r2_score(y_test, y_hat)}')
		print(f'MAE: {mean_absolute_error(y_test, y_hat)}')

	def metricas_clasificacion(self, y_test, y_hat):
		print(f'Exactitud: {accuracy_score(y_test, y_hat)}')
		print(f'Recall: {recall_score(y_test, y_hat)}')
		print(f'Exactitud F1: {f1_score(y_test, y_hat)}')
		print(f'Precision: {precision_score(y_test, y_hat)}')

	def metricas_general(self, y_test, y_hat):
		print(f'Matriz de confusion: {confusion_matrix(y_test, y_hat)}')
		print(f'Reporte: \n{classification_report(y_test, y_hat)}')