package main

import (
	"github.com/labstack/echo/v4"
	"zadanie4/controller"
	"zadanie4/models"
	"zadanie4/routes"
)

func main() {
	e := echo.New()

	products := []models.Product{
		{ID: 1, Name: "Książka", Price: 29.99},
		{ID: 2, Name: "Laptop", Price: 999.99},
		{ID: 3, Name: "Smartfon", Price: 699.99},
	}

	controller.Products = products

	routes.RegisterProductRoutes(e)

	e.Logger.Fatal(e.Start(":8080"))
}
