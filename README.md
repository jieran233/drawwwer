# drawwwer
 draw and guess!

![](https://s2.loli.net/2023/08/26/CxskTmuZpXzgqUF.png)

## Usage

- Install [stable-diffusion-webui](https://github.com/AUTOMATIC1111/stable-diffusion-webui) and install [sd-webui-controlnet](https://github.com/Mikubill/sd-webui-controlnet) plugin
- Open SD WebUI and jump to ControlNet
  ![](https://s2.loli.net/2023/08/26/ju2QpcPCobIgtlL.png)
- Run `python drawer.py <image_path>`
  - Confirm processed image in the popup window, close it to continue
  - After 5 seconds, the program will start drawing 

## Feature

- `scale`

  Set scale of drawing
- `draw_position_point` (new!)

  Draw the four corners of the picture to prevent misoperation caused by high-frequency automatic clicks

  I believe you wouldn't want it to frantically click on your taskbar applications and then stage such a scene:

  <img src="https://s2.loli.net/2023/08/27/qsk2YL19ZmuSbrP.jpg" alt="🤣👉" width="30%">
- `interlaced` (new!)

  🤣👉The actual test results show that there is almost no difference between interlaced scanning and progressive scanning in terms of time and GPU utilization.

## Roadmap

- [Add PySide6 GUI](https://www.youtube.com/watch?v=dQw4w9WgXcQ)