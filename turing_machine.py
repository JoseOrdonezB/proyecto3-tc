# turing_machine.py
from dataclasses import dataclass
from typing import Dict, Tuple, List, Iterable


@dataclass
class Transition:
    next_state: str
    write_symbol: str
    move: str


TransitionKey = Tuple[str, str]
TransitionTable = Dict[TransitionKey, Transition]


def build_transition_table(mt_config: dict) -> TransitionTable:
    table: TransitionTable = {}

    for rule in mt_config.get("transitions", []):
        state = rule["state"]
        reads = rule["read"]
        writes = rule["write"]
        move = rule["move"]
        next_state = rule["next"]

        if len(reads) != len(writes):
            raise ValueError(
                f"Regla inválida en estado {state}: 'read' y 'write' "
                f"deben tener la misma cantidad de símbolos."
            )

        if move not in ("L", "R"):
            raise ValueError(
                f"Movimiento inválido en regla de estado {state}: {move}. "
                "Debe ser 'L' o 'R'."
            )

        for read_symbol, write_symbol in zip(reads, writes):
            key: TransitionKey = (state, read_symbol)
            if key in table:
                raise ValueError(
                    f"Transición duplicada para ({state}, {read_symbol})"
                )

            table[key] = Transition(
                next_state=next_state,
                write_symbol=write_symbol,
                move=move,
            )

    return table


class TuringMachine:
    def __init__(self, mt_config: dict) -> None:
        self.states: List[str] = list(mt_config["states"])
        self.input_alphabet = set(mt_config["input_alphabet"])
        self.tape_alphabet = set(mt_config["tape_alphabet"])
        self.initial_state: str = mt_config["initial_state"]
        self.accept_states = set(mt_config["accept_states"])

        self.blank_symbol: str = mt_config.get("blank_symbol", "B")

        if self.blank_symbol not in self.tape_alphabet:
            raise ValueError(
                f"El símbolo blanco '{self.blank_symbol}' no está en el alfabeto de cinta."
            )

        self.transitions: TransitionTable = build_transition_table(mt_config)

    def _ensure_head_in_range(self, tape: List[str], head: int) -> Tuple[List[str], int]:
        if head < 0:
            tape.insert(0, self.blank_symbol)
            head = 0
        elif head >= len(tape):
            tape.append(self.blank_symbol)
        return tape, head

    def _format_id(self, tape: List[str], head: int, state: str) -> str:
        parts: List[str] = []
        for i, symbol in enumerate(tape):
            if i == head:
                parts.append(f"[{state}]")
            parts.append(symbol)
        return " ".join(parts)

    def run(
        self,
        input_string: str,
        max_steps: int = 10_000,
    ) -> dict:
        if input_string:
            tape: List[str] = list(input_string)
        else:
            tape = [self.blank_symbol]

        state: str = self.initial_state
        head: int = 0
        steps: int = 0

        ids: List[str] = []
        ids.append(self._format_id(tape, head, state))

        while True:
            if max_steps is not None and steps >= max_steps:
                break

            current_symbol = tape[head]
            key: TransitionKey = (state, current_symbol)

            if key not in self.transitions:
                break

            transition = self.transitions[key]

            tape[head] = transition.write_symbol
            state = transition.next_state

            if transition.move == "R":
                head += 1
            elif transition.move == "L":
                head -= 1
            else:
                raise ValueError(f"Movimiento inválido: {transition.move}")

            tape, head = self._ensure_head_in_range(tape, head)

            ids.append(self._format_id(tape, head, state))

            steps += 1

        accepted = state in self.accept_states

        final_tape_str = "".join(tape).rstrip(self.blank_symbol)

        return {
            "accepted": accepted,
            "final_state": state,
            "final_tape": final_tape_str,
            "ids": ids,
        }

    def run_multiple(self, inputs: Iterable[str], max_steps: int = 10_000) -> Dict[str, dict]:
        results: Dict[str, dict] = {}
        for w in inputs:
            results[w] = self.run(w, max_steps=max_steps)
        return results
