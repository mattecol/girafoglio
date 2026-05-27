from __future__ import annotations

import argparse

from girafoglio import HeadMovementPageTurner, TurnEvent


def run_simulation() -> None:
    turner = HeadMovementPageTurner()
    print("Modalità simulata attiva. Inserisci un valore di yaw per riga.")

    while True:
        try:
            raw = input("> ").strip()
        except EOFError:
            print("\nChiusura.")
            return

        if not raw:
            continue

        try:
            yaw = float(raw)
        except ValueError:
            print("Valore non valido. Inserisci un numero.")
            continue

        event = turner.process_yaw(yaw)
        if event == TurnEvent.NEXT:
            print("➡️ Pagina successiva")
        elif event == TurnEvent.PREVIOUS:
            print("⬅️ Pagina precedente")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Gira spartiti con movimenti della testa."
    )
    parser.add_argument(
        "--simulate",
        action="store_true",
        help="Usa input testuale per simulare il tracciamento della testa.",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    if args.simulate:
        run_simulation()
        return

    print(
        "Avvia con --simulate per la demo testuale. "
        "Puoi integrare un tracker webcam richiamando process_yaw()."
    )


if __name__ == "__main__":
    main()
