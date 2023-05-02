#!/usr/bin/bash

read -p "Enter the file name: " file_name

touch "$file_name"

echo "#!/usr/bin/env python3" > "$file_name"
chmod a+x "$file_name"
