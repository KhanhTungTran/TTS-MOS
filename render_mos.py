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
                    "title" : "Question " + str(i),
                    "audio_paths": ["wavs/q"+str(i)+"/test1.wav","wavs/q"+str(i)+"/test2.wav","wavs/q"+str(i)+"/test3.wav","wavs/q"+str(i)+"/test4.wav","wavs/q"+str(i)+"/test5.wav"],
                    "name": "q" + str(i)} for i in range(1,NUM+1)]
    )
    with open("rendered_mos_v2.html", "w", encoding="utf-8") as f:
        f.write(html)


if __name__ == "__main__":
    main()
