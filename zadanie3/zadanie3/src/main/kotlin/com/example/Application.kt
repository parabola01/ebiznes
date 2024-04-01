package com.example

import io.ktor.client.*
import io.ktor.client.engine.cio.*
import io.ktor.client.plugins.contentnegotiation.*
import io.ktor.client.request.*
import io.ktor.client.statement.*
import io.ktor.http.*
import io.ktor.http.content.*
import io.ktor.server.application.*
import io.ktor.server.engine.*
import io.ktor.server.netty.*
import io.ktor.server.response.*
import io.ktor.server.routing.*
import io.ktor.util.*
import kotlinx.coroutines.Dispatchers
import kotlinx.coroutines.withContext
import io.ktor.serialization.kotlinx.json.*
import io.ktor.server.request.*
import kotlinx.serialization.Serializable
import kotlinx.serialization.json.Json
import kotlinx.serialization.encodeToString

fun main() {
    embeddedServer(Netty, port = 8080) {
        module()
    }.start(wait = true)
}

@Serializable
data class DiscordMessage(val content: String)

fun Application.module() {
    routing {
        get("/") {
            call.respondText("Witaj w aplikacji Ktor!", ContentType.Text.Html)
        }
        post("/send-message") {
            try {
                val receivedText = call.receiveText()
                val receivedMessage = Json.decodeFromString<DiscordMessage>(receivedText)
                val messageStatus = sendMessageToDiscord(receivedMessage.content)
                call.respondText(messageStatus)
            } catch (e: Exception) {
                call.respondText("Error : ${e.localizedMessage}")
            }
        }
    }
}

@OptIn(InternalAPI::class)
suspend fun sendMessageToDiscord(message: String): String = withContext(Dispatchers.IO) {
    val client = HttpClient(CIO) {
        install(ContentNegotiation) {
            json(Json{
                isLenient = true
                ignoreUnknownKeys = true
            })
        }
    }

    try {
        val jsonBody = Json.encodeToString(DiscordMessage(message))
        val response: HttpResponse = client.post("https://discord.com/api/webhooks/1221542003897143296/s6Dce2G3eg8Q-JzZ2XkqOe-T527MgFpp7BGiiGsWWyHWoP34zsWyxsLyVWNAx-tqcSkE") {
            contentType(ContentType.Application.Json)
            body = TextContent(jsonBody, ContentType.Application.Json)
        }
        "Wiadomość wysłana: ${response.bodyAsText()}"
    } catch (e: Exception) {
        "Błąd podczas wysyłania wiadomości: ${e.message}"
    } finally {
        client.close()
    }
}