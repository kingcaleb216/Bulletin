def generate_collapsible_html(lyrics, number, title):
    paragraphs = [para.strip().replace('\n', '<br>') for para in lyrics.strip().split('\n\n')]
    html = f'<div class="section">\n'
    html += f'    <button class="collapsible">{number}: {title} <span class="icon">+</span></button>\n'
    html += f'    <div class="content">\n'

    for i, para in enumerate(paragraphs):
        tag_open = '<b><p>' if i % 2 == 1 else '<p>'
        tag_close = '</p></b>' if i % 2 == 1 else '</p>'
        html += f'        {tag_open}{para}{tag_close}\n\n'

    html += f'    </div>\n</div>'
    return html

# Example usage:
lyrics = """
God sent His son,
They called Him, Jesus;
He came to love,
Heal and forgive;
He lived and died
To buy my pardon,
An empty grave is there
To prove my Savior lives!

Because He lives,
I can face tomorrow!
Because He lives,
All fear is gone.
Because I know
He holds the future,
And life is worth the living,
Just because He lives!

How sweet to hold
A newborn baby,
And feel the pride
And joy he brings;
But greater still
The calm assurance:
This child can face
Uncertain days because He Lives!

Because He lives,
I can face tomorrow!
Because He lives,
All fear is gone.
Because I know
He holds the future,
And life is worth the living,
Just because He lives!

And then one day,
I'll cross the river,
I'll fight life's final
War with pain;
And then, as death
Gives way to victory,
I'll see the lights of glory
And I'll know He lives!

Because He lives,
I can face tomorrow!
Because He lives,
All fear is gone.
Because I know
He holds the future,
And life is worth the living,
Just because He lives!
"""

print(generate_collapsible_html(lyrics, "407", "Because He Lives"))
