package routes

import (
	"backend/controller"
	"github.com/labstack/echo/v4"
)

func RegisterProductRoutes(e *echo.Echo) {
	e.GET("/products", controller.GetProducts)
	e.GET("/products/:id", controller.GetProduct)
	e.POST("/products", controller.CreateProduct)
	e.PUT("/products/:id", controller.UpdateProduct)
	e.DELETE("/products/:id", controller.DeleteProduct)
}
