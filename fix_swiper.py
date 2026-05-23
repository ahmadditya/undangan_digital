import re

with open('/Applications/XAMPP/xamppfiles/htdocs/undangan/index.html', 'r') as f:
    content = f.read()

# Extract #story section
story_pattern = r'(<section id="story".*?</section>)'
story_match = re.search(story_pattern, content, re.DOTALL)
if story_match:
    story_html = story_match.group(1)
    
    # In story_html, replace images, titles, and subtitles
    # Images 1 to 5
    images = [
        "img/bg-prewed.jpg",
        "https://picsum.photos/400/600?random=1",
        "https://picsum.photos/400/600?random=2",
        "https://picsum.photos/400/600?random=3",
        "https://picsum.photos/400/600?random=4"
    ]
    
    # we need to replace the first 5 src="assets/img/X.jpg" with these
    for i in range(1, 6):
        story_html = re.sub(rf'assets/img/{i}\.jpg', images[i-1], story_html)
        
    # Replace texts
    story_html = story_html.replace('gambar', 'Romeo & Juliet')
    story_html = story_html.replace('di sini yaa', 'Prewedding Moment')
    
    # Remove extra slides if any (6, 7) or just let them be replaced with randoms
    story_html = story_html.replace('assets/img/6.jpg', 'https://picsum.photos/400/600?random=5')
    story_html = story_html.replace('assets/img/7.jpg', 'https://picsum.photos/400/600?random=6')
    
    # write back
    new_content = content.replace(story_match.group(1), story_html)
    
    # Also fix #gallery section just in case text needs update
    
    with open('/Applications/XAMPP/xamppfiles/htdocs/undangan/index.html', 'w') as f:
        f.write(new_content)
    print("Fixed Swiper content in #story")
else:
    print("Story section not found")
