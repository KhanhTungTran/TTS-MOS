#!/usr/bin/env python3
"""Generate forms for human evaluation."""

from jinja2 import FileSystemLoader, Environment

NUM = 40

def main():
    """Main function."""
    loader = FileSystemLoader(searchpath="./templates")
    env = Environment(loader=loader)
    template = env.get_template("mos.html.jinja2")

    html = template.render(
        page_title="MOS Experiment Form 1",
        form_url="https://script.google.com/macros/s/AKfycbzApm3cSoTRMbhTaEgd3c3VtpV9nRP1DUqxXQLsyVz9uAtTrSty/exec",
        form_id=1,
        questions=[{
                    "title" : "Question " + str(i+1),
                    "audio_paths": ["wavs/test1.wav","wavs/test2.wav","wavs/test3.wav","wavs/test4.wav"],
                    "name": "q" + str(i+1)} for i in range(NUM)]
    )
    with open("rendered_mos.html", "w", encoding="utf-8") as f:
        f.write(html)


if __name__ == "__main__":
    main()
