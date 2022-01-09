#!/usr/bin/env python3
"""Generate forms for human evaluation."""

from jinja2 import FileSystemLoader, Environment


def main():
    """Main function."""
    loader = FileSystemLoader(searchpath="./templates")
    env = Environment(loader=loader)
    template = env.get_template("mos.html.jinja2")

    html = template.render(
        page_title="MOS Experiment Form 1",
        form_url="https://script.googleusercontent.com/a/macros/hcmut.edu.vn/echo?user_content_key=Eu-JMluz1jbTPtY6iFrR6kpaLppVF-GPPxDHqjEvW_LKjGXy3JU13Dly4-JSUkhmcBdr8apTz9p-76TdGkiYTisoTXXOUydFm5_BxDlH2jW0nuo2oDemN9CCS2h10ox_nRPgeZU6HP-kBB7dw9cxQg-axdEUzoD4h0lmODcuY_0u0-uhyqDm_cXfVzxRl393pKVIncqArub0GP-If4GSGem-6CwWxbcCdoSaqL2SwsZLpwlMMG3mig&lib=M12yLyt9Zl8s8EiKk1VyYdRcha9aOzO03",
        form_id=1,
        questions=[
            {
                "title": "Question 1",
                "audio_paths": ["wavs/test1.wav","wavs/test2.wav"],
                "name": "q1"
            },
            {
                "title": "Question 2",
                "audio_paths": ["wavs/test1.wav","wavs/test2.wav"],
                "name": "q2"
            },
        ]
    )
    print(html)


if __name__ == "__main__":
    main()
