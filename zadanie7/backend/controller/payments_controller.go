package controller

import (
	"github.com/labstack/echo/v4"
	"net/http"
	"strconv"

	"backend/models"
)

var Payments []models.Payment

func GetPayments(c echo.Context) error {
	return c.JSON(http.StatusOK, Payments)
}

func GetPayment(c echo.Context) error {
	_, err := strconv.Atoi(c.Param("id"))
	if err != nil {
		return c.String(http.StatusBadRequest, "Błędny parametr ID")
	}

	for _, payment := range Payments {
		if strconv.Itoa(payment.ID) == c.Param("id") {
			return c.JSON(http.StatusOK, payment)
		}
	}
	return c.String(http.StatusNotFound, "Płatność o podanym ID nie została znaleziona")
}

func CreatePayment(c echo.Context) error {
	payment := new(models.Payment)
	if err := c.Bind(payment); err != nil {
		return err
	}

	for _, p := range Payments {
		if p.ID == payment.ID {
			return c.String(http.StatusConflict, "Płatność o podanym ID już istnieje")
		}
	}

	Payments = append(Payments, *payment)
	return c.JSON(http.StatusCreated, payment)
}

func UpdatePayment(c echo.Context) error {
	_, err := strconv.Atoi(c.Param("id"))
	if err != nil {
		return c.String(http.StatusBadRequest, "Błędny parametr ID")
	}

	for i, payment := range Payments {
		if strconv.Itoa(payment.ID) == c.Param("id") {
			updatedPayment := new(models.Payment)
			if err := c.Bind(updatedPayment); err != nil {
				return err
			}
			Payments[i] = *updatedPayment
			return c.JSON(http.StatusOK, Payments[i])
		}
	}
	return c.String(http.StatusNotFound, "Płatność o podanym ID nie została znaleziona")
}

func DeletePayment(c echo.Context) error {
	_, err := strconv.Atoi(c.Param("id"))
	if err != nil {
		return c.String(http.StatusBadRequest, "Błędny parametr ID")
	}

	for i, payment := range Payments {
		if strconv.Itoa(payment.ID) == c.Param("id") {
			Payments = append(Payments[:i], Payments[i+1:]...)
			return c.NoContent(http.StatusNoContent)
		}
	}
	return c.String(http.StatusNotFound, "Płatność o podanym ID nie została znaleziona")
}
