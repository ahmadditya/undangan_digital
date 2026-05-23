import re

with open('/Applications/XAMPP/xamppfiles/htdocs/undangan/index.html', 'r') as f:
    content = f.read()

# Extract Bootstrap Carousel from #story
carousel_pattern = r'(<div class="col-md-6 col-10 mx-auto">\s*<div class="prewedding-card".*?</div>\s*</div>\s*</div>)'
carousel_match = re.search(carousel_pattern, content, re.DOTALL)
if carousel_match:
    carousel_html = carousel_match.group(1)
else:
    print("Carousel not found")
    exit(1)

# Extract Swiper from #gallery
swiper_pattern = r'(<center>\s*<!-- =============== SWIPER GALLERY CARDS =============== -->.*?</div>\s*</center>)'
swiper_match = re.search(swiper_pattern, content, re.DOTALL)
if swiper_match:
    swiper_html = swiper_match.group(1)
else:
    print("Swiper not found")
    exit(1)

# Swap them
content = content.replace(carousel_html, "<!-- TEMP_CAROUSEL -->")
content = content.replace(swiper_html, "<!-- TEMP_SWIPER -->")

content = content.replace("<!-- TEMP_CAROUSEL -->", swiper_html)
content = content.replace("<!-- TEMP_SWIPER -->", carousel_html)

with open('/Applications/XAMPP/xamppfiles/htdocs/undangan/index.html', 'w') as f:
    f.write(content)

print("Swapped successfully")
