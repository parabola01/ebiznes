package controller

import (
	"net/http"
	"strconv"

	"github.com/labstack/echo/v4"
	"zadanie4/models"
)

var Products []models.Product

func GetProducts(c echo.Context) error {
	return c.JSON(http.StatusOK, Products)
}

func GetProduct(c echo.Context) error {
	_, err := strconv.Atoi(c.Param("id"))
	if err != nil {
		return c.String(http.StatusBadRequest, "Błędny parametr ID")
	}

	for _, p := range Products {
		if strconv.Itoa(p.ID) == c.Param("id") {
			return c.JSON(http.StatusOK, p)
		}
	}
	return c.String(http.StatusNotFound, "Produkt o podanym ID nie został znaleziony")
}

func CreateProduct(c echo.Context) error {
	product := new(models.Product)
	if err := c.Bind(product); err != nil {
		return err
	}

	for _, p := range Products {
		if p.ID == product.ID {
			return c.String(http.StatusConflict, "Produkt o podanym ID już istnieje")
		}
	}

	Products = append(Products, *product)
	return c.JSON(http.StatusCreated, product)
}

func UpdateProduct(c echo.Context) error {
	_, err := strconv.Atoi(c.Param("id"))
	if err != nil {
		return c.String(http.StatusBadRequest, "Błędny parametr ID")
	}

	for i, p := range Products {
		if strconv.Itoa(p.ID) == c.Param("id") {
			updatedProduct := new(models.Product)
			if err := c.Bind(updatedProduct); err != nil {
				return err
			}
			Products[i] = *updatedProduct
			return c.JSON(http.StatusOK, Products[i])
		}
	}
	return c.String(http.StatusNotFound, "Produkt o podanym ID nie został znaleziony")
}

func DeleteProduct(c echo.Context) error {
	_, err := strconv.Atoi(c.Param("id"))
	if err != nil {
		return c.String(http.StatusBadRequest, "Błędny parametr ID")
	}

	for i, p := range Products {
		if strconv.Itoa(p.ID) == c.Param("id") {
			Products = append(Products[:i], Products[i+1:]...)
			return c.NoContent(http.StatusNoContent)
		}
	}
	return c.String(http.StatusNotFound, "Produkt o podanym ID nie został znaleziony")
}
