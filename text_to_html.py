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
I serve a risen Saviour, He's in the world today
I know that He is living, whatever men may say
I see His hand of mercy, I hear His voice of cheer
And just the time I need Him He's always near

He lives! He lives! Christ Jesus lives today!
He walks with me and talks with me
Along life's narrow way
He lives! He lives! Salvation to impart!
You ask me how I know He lives?
He lives within my heart

In all the world around me I see His loving care
And though my heart grows weary I never will despair
I know that He is leading, thro' all the stormy blast
The day of His appearing will come at last

He lives! He lives! Christ Jesus lives today!
He walks with me and talks with me
Along life's narrow way
He lives! He lives! Salvation to impart!
You ask me how I know He lives?
He lives within my heart

Rejoice, rejoice, O Christian! Lift up your voice and sing
Eternal hallelujahs to Jesus Christ, the King!
The Hope of all who seek Him, the Help of all who find
None other is so loving, so good and kind

He lives! He lives! Christ Jesus lives today!
He walks with me and talks with me
Along life's narrow way
He lives! He lives! Salvation to impart!
You ask me how I know He lives?
He lives within my heart
"""

print(generate_collapsible_html(lyrics, "407", "Because He Lives"))
