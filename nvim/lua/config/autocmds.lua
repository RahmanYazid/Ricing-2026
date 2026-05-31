vim.api.nvim_create_autocmd("ColorScheme", {
  pattern = "*",
  callback = function()
    -- transparency
    vim.api.nvim_set_hl(0, "Normal", { bg = "none" })
    vim.api.nvim_set_hl(0, "NormalFloat", { bg = "none" })
    vim.api.nvim_set_hl(0, "NormalNC", { bg = "none" })
    vim.api.nvim_set_hl(0, "SignColumn", { bg = "none" })
    vim.api.nvim_set_hl(0, "LineNr", { bg = "none" })
    vim.api.nvim_set_hl(0, "EndOfBuffer", { bg = "none" })

    -- bold + italic biar lebih popup
    vim.api.nvim_set_hl(0, "Keyword", { bold = true, italic = true })
    vim.api.nvim_set_hl(0, "Function", { bold = true })
    vim.api.nvim_set_hl(0, "Type", { bold = true })
    vim.api.nvim_set_hl(0, "Tag", { bold = true, fg = "#E4670B" })
    vim.api.nvim_set_hl(0, "Comment", { italic = true, fg = "#a18f70" })
    vim.api.nvim_set_hl(0, "String", { italic = true, fg = "#DE9D13" })
    vim.api.nvim_set_hl(0, "Constant", { bold = true, fg = "#AE9005" })
  end,
})
