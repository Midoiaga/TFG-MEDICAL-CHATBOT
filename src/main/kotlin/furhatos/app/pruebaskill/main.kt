package furhatos.app.pruebaskill

import furhatos.app.pruebaskill.flow.*
import furhatos.skills.Skill
import furhatos.flow.kotlin.*

class PruebaskillSkill : Skill() {
    override fun start() {
        Flow().run(Idle)
    }
}

fun main(args: Array<String>) {
    Skill.main(args)
}
