# pptx_handler.py
from pptx import Presentation
from copy import deepcopy

def load_presentation(file_path):
    """Load the original presentation."""
    return Presentation(file_path)

def extract_slide_text(slide):
    """Extract all text from shapes in a slide."""
    text_elements = []
    for shape in slide.shapes:
        if shape.has_text_frame:
            text_elements.append(shape.text)
    return "\n".join(text_elements)

def generate_translated_pptx(input_path, output_path, target_lang):
    prs = load_presentation(input_path)
    new_prs = Presentation()

    for slide_index, slide in enumerate(prs.slides, start=1):
        layout = slide.slide_layout  # Make sure this is defined at the top of the loop
    
        # Original slide
        original_slide = new_prs.slides.add_slide(layout)
        copy_slide_text(slide, original_slide, translate=False)
    
        # Translated slide
        translated_slide = new_prs.slides.add_slide(layout)
        copy_slide_text(slide, translated_slide, translate=True, target_lang=target_lang)

        # Add original slide
        #original_slide = new_prs.slides.add_slide(slide.slide_layout)
        for i, shape in enumerate(slide.shapes):
            if shape.has_text_frame:
                try:
                    original_slide.shapes[i].text = shape.text
                except IndexError:
                    continue

        # 🌐 Translated Slide

    new_prs.save(output_path)
    print(f"Saved translated presentation to: {output_path}")

def copy_slide_text(source_slide, target_slide, translate=False, target_lang='en'):
    """
    Copy text from source_slide to target_slide.
    If translate=True, the text is translated to target_lang.
    """
    from translator import translate_text  # Local import to avoid circular dependency

    for shape in source_slide.shapes:
        if not shape.has_text_frame:
            continue

        # Try to find a matching shape in the target slide by shape type/position
        # Fallback: Add a new textbox in roughly the same location
        try:
            left = shape.left
            top = shape.top
            width = shape.width
            height = shape.height
            new_shape = target_slide.shapes.add_textbox(left, top, width, height)

            original_text = shape.text
            new_text = translate_text(original_text, target_lang) if translate else original_text
            new_shape.text_frame.text = new_text
        except Exception as e:
            print(f"[⚠️] Failed to duplicate a shape: {e}")

def translate_text_in_place(pptx_path, output_path, target_lang):
    from translator import translate_text
    prs = Presentation(pptx_path)

    for slide in prs.slides:
        for shape in slide.shapes:
            if shape.has_text_frame:
                original_text = shape.text
                translated_text = translate_text(original_text, target_lang)
                shape.text = translated_text  # Keep format, swap text

    prs.save(output_path)
    print(f"✔️ Translated (in-place) file saved to: {output_path}")

