package routes

import (
	"backend/controller"
	"github.com/labstack/echo/v4"
)

func RegisterPaymentRoutes(e *echo.Echo) {

	e.GET("/payments", controller.GetPayments)
	e.GET("/payments/:id", controller.GetPayment)
	e.POST("/payments", controller.CreatePayment)
	e.PUT("/payments/:id", controller.UpdatePayment)
	e.DELETE("/payments/:id", controller.DeletePayment)
}
