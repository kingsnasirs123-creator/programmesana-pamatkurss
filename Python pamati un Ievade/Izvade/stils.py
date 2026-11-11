"""Programma simulē spēles personāža veselības punktu (HP) samazināšanos,
kad tam uzbrūk pretinieks ar noteiktu spēku."""

speletaja_vards = "Anna"
hp_punkti = 100
uzbrukuma_jauda = 25
# Pretinieka veiksmīga uzbrukuma rezultātā spēlētājs zaudē veselību, tāpēc no kopējiem HP tiek atskaitīts saņemtais kaitējums
atlikušie_hp_punkti = hp_punkti - uzbrukuma_jauda