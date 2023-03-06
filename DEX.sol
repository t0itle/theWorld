DEX

pragma solidity ^0.8.0;

import "https://github.com/OpenZeppelin/openzeppelin-contracts/contracts/token/ERC721/ERC721.sol";

contract GameExchange {
    using SafeMath for uint256;

    ERC721 public items;
    mapping(address => mapping(uint256 => bool)) public itemOwnership;
    mapping(address => uint256) public itemPrices;
    mapping(address => mapping(address => bool)) public characterOwnership;
    mapping(address => uint256) public characterPrices;
    mapping(address => mapping(address => bool)) public npcOwnership;
    mapping(address => uint256) public npcPrices;

    constructor() public {
        items = new ERC721("Items", "ITM");
    }

    function mintItem(string memory _name, string memory _description, uint256 _price) public {
        require(msg.sender == address(items), "Only the item contract can mint new items.");
        uint256 itemId = items.totalSupply();
        items.mint(msg.sender, itemId);
        itemOwnership[msg.sender][itemId] = true;
        itemPrices[itemId] = _price;
        items.setTokenURI(itemId, stringToBytes32(_name), stringToBytes32(_description));
    }

    function mintCharacter(string memory _name, string memory _description, uint256 _price) public {
        require(msg.sender == address(items), "Only the item contract can mint new characters.");
        uint256 characterId = items.totalSupply();
        items.mint(msg.sender, characterId);
        characterOwnership[msg.sender][characterId] = true;
        characterPrices[characterId] = _price;
        items.setTokenURI(characterId, stringToBytes32(_name), stringToBytes32(_description));
    }

    function mintNpc(string memory _name, string memory _description, uint256 _price) public {
        require(msg.sender == address(items), "Only the item contract can mint new NPCs.");
        uint256 npcId = items.totalSupply();
        items.mint(msg.sender, npcId);
        npcOwnership[msg.sender][npcId] = true;
        npcPrices[npcId] = _price;
        items.setTokenURI(npcId, stringToBytes32(_name), stringToBytes32(_description));
    }

    function buyItem(uint256 _itemId) public payable {
        require(itemOwnership[msg.sender][_itemId] == false, "You already own this item.");
        require(itemPrices[_itemId] <= msg.value, "The price of the item is higher than the sent ether.");
        address itemOwner = items.ownerOf(_itemId);
        itemOwner.transfer(itemPrices[_itemId]);
        itemOwnership[msg.sender
pragma solidity ^0.8.0;

contract DEX {
    // Mapping of tokens (items, characters, etc.) to their ownership details
    mapping (address => mapping (address => uint256)) public tokenOwnership;
    
    // Mapping of tokens to their metadata (name, description, etc.)
    mapping (address => string) public tokenName;
    mapping (address => string) public tokenDescription;
    
    // Events to signal a successful trade
    event Trade(address indexed _from, address indexed _to, address indexed _token, uint256 _value);
    
    // Function to approve a transfer of a token
    function approve(address _token, address _spender) public {
        require(msg.sender == tokenOwnership[_token][msg.sender]);
        require(_spender != address(0));
        tokenOwnership[_token][_spender] = true;
    }
    
    // Function to trade a token
    function trade(address _token, address _to, uint256 _value) public {
        require(tokenOwnership[_token][msg.sender]);
        require(tokenOwnership[_token][_to] || _to == address(0));
        require(_value > 0);
        
        // Transfer ownership of the token
        tokenOwnership[_token][msg.sender] = false;
        tokenOwnership[_token][_to] = true;
        
        // Transfer value (gold, experience points, etc.)
        msg.sender.transfer(_value);
        _to.transfer(_value);
        
        // Emit a trade event
        emit Trade(msg.sender, _to, _token, _value);
    }
}
