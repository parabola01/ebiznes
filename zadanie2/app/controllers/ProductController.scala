package controllers

import play.api.mvc._
import play.api.libs.json._
import javax.inject.Inject

// Klasa kontrolera produktów
class ProductController @Inject()(val controllerComponents: ControllerComponents) extends BaseController {
  
  var products = Seq(
    Product(1, "Książka", 29.99),
    Product(2, "Telefon", 499.99),
    Product(3, "Laptop", 999.99)
  )

  def getProducts() = Action { implicit request: Request[AnyContent] =>
    Ok(Json.toJson(products))
  }

  def getProduct(id: Int) = Action { implicit request: Request[AnyContent] =>
    products.find(_.id == id) match {
      case Some(product) => Ok(Json.toJson(product))
      case None => NotFound("Produkt o podanym ID nie istnieje.")
    }
  }

  def addProduct() = Action(parse.json) { implicit request =>
    request.body.validate[Product] match {
      case JsSuccess(product, _) =>
        if (products.exists(_.id == product.id)) {
          BadRequest("Produkt o podanym ID już istnieje.")
        } else {
          products = products :+ product
          Created(Json.toJson(product))
        }
      case JsError(errors) =>
        BadRequest("Nieprawidłowe dane produktu.")
    }
  }

def updateProduct(id: Int) = Action(parse.json) { implicit request =>
  request.body.validate[Product] match {
    case JsSuccess(updatedProduct, _) =>
      if (products.exists(p => p.id != id && p.id == updatedProduct.id)) {
        BadRequest("Produkt o podanym ID już istnieje.")
      } else {
        products.find(_.id == id) match {
          case Some(_) =>
            products = products.filterNot(_.id == id) :+ updatedProduct.copy(id = id)
            Ok(Json.toJson(updatedProduct))
          case None =>
            NotFound("Produkt o podanym ID nie istnieje.")
        }
      }
    case JsError(errors) =>
      BadRequest("Nieprawidłowe dane produktu.")
  }
}


  def deleteProduct(id: Int) = Action { implicit request =>
    products.find(_.id == id) match {
      case Some(_) =>
        products = products.filterNot(_.id == id)
        NoContent
      case None =>
        NotFound("Produkt o podanym ID nie istnieje.")
    }
  }
}

case class Product(id: Int, name: String, price: Double)

object Product {
  implicit val format: OFormat[Product] = Json.format[Product]
}

