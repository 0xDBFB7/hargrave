
Drivers are called by; primarily for instruments.

If you want to connect your own code, use a language binding.

I think Hargrave drivers should only implement the glue logic between an instrument's API and the Hargrave db. If a driver might be useful more generally, it should be spun out into its own repository and called by a driver.

