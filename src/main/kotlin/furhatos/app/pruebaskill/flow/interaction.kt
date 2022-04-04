package furhatos.app.pruebaskill.flow

import furhatos.nlu.common.*
import furhatos.flow.kotlin.*
import furhatos.flow.kotlin.furhat.System.logger

val Start : State = state(Interaction) {

    onEntry {
        logger.info("eyy2")
        Runtime.getRuntime().exec("python crear.py")
        furhat.ask("Hi there. Do you like robots?")
    }

    onResponse<Yes>{
        furhat.say("I like humans.")
    }

    onResponse<No>{
        furhat.say("That's sad.")
    }
}
