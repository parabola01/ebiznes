package main

import (
	"backend/routes"
	"github.com/labstack/echo/v4"
	"github.com/labstack/echo/v4/middleware"
)

func main() {

	e := echo.New()

	e.Use(middleware.CORSWithConfig(middleware.CORSConfig{
		AllowOrigins: []string{"*"},
		AllowMethods: []string{echo.GET, echo.PUT, echo.POST, echo.DELETE},
	}))

	routes.RegisterProductRoutes(e)

	routes.RegisterPaymentRoutes(e)

	e.Logger.Fatal(e.Start(":8080"))
}
